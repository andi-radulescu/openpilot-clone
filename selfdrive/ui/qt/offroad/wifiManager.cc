#include "selfdrive/ui/qt/offroad/wifiManager.h"

#include <algorithm>
#include <set>
#include <cstdlib>

#include "selfdrive/common/params.h"
#include "selfdrive/common/swaglog.h"

template <typename T>
T get_response(QDBusMessage response) {
  QVariant first =  response.arguments().at(0);
  QDBusVariant dbvFirst = first.value<QDBusVariant>();
  QVariant vFirst = dbvFirst.variant();
  if (vFirst.canConvert<T>()) {
    return vFirst.value<T>();
  } else {
    LOGE("Variant unpacking failure");
    return T();
  }
}

bool compare_by_strength(const Network &a, const Network &b) {
  if (a.connected == ConnectedType::CONNECTED) return true;
  if (b.connected == ConnectedType::CONNECTED) return false;
  if (a.connected == ConnectedType::CONNECTING) return true;
  if (b.connected == ConnectedType::CONNECTING) return false;
  return a.strength > b.strength;
}

WifiManager::WifiManager(QWidget* parent) : QWidget(parent) {
  qDBusRegisterMetaType<Connection>();
  qDBusRegisterMetaType<IpConfig>();
  connecting_to_network = "";

  // Set tethering ssid as "weedle" + first 4 characters of a dongle id
  tethering_ssid = "weedle";
  std::string bytes = Params().get("DongleId");
  if (bytes.length() >= 4) {
    tethering_ssid += "-" + QString::fromStdString(bytes.substr(0,4));
  }

  adapter = getAdapter();
  if (!adapter.isEmpty()) {
    setup();
  } else {
    bus.connect(NM_DBUS_SERVICE, NM_DBUS_PATH, NM_DBUS_INTERFACE, "DeviceAdded", this, SLOT(deviceAdded(QDBusObjectPath)));
  }

  QTimer* timer = new QTimer(this);
  QObject::connect(timer, &QTimer::timeout, this, [=]() {
    if (!adapter.isEmpty() && this->isVisible()) {
      requestScan();
    }
  });
  timer->start(5000);
}

void WifiManager::setup() {
  QDBusInterface nm(NM_DBUS_SERVICE, adapter, NM_DBUS_INTERFACE_DEVICE, bus);
  bus.connect(NM_DBUS_SERVICE, adapter, NM_DBUS_INTERFACE_DEVICE, "StateChanged", this, SLOT(stateChange(unsigned int, unsigned int, unsigned int)));
  bus.connect(NM_DBUS_SERVICE, adapter, NM_DBUS_INTERFACE_PROPERTIES, "PropertiesChanged", this, SLOT(propertyChange(QString, QVariantMap, QStringList)));

  bus.connect(NM_DBUS_SERVICE, NM_DBUS_PATH_SETTINGS, NM_DBUS_INTERFACE_SETTINGS, "ConnectionRemoved", this, SLOT(connectionRemoved(QDBusObjectPath)));
  bus.connect(NM_DBUS_SERVICE, NM_DBUS_PATH_SETTINGS, NM_DBUS_INTERFACE_SETTINGS, "NewConnection", this, SLOT(newConnection(QDBusObjectPath)));

  QDBusInterface device_props(NM_DBUS_SERVICE, adapter, NM_DBUS_INTERFACE_PROPERTIES, bus);
  device_props.setTimeout(DBUS_TIMEOUT);
  QDBusMessage response = device_props.call("Get", NM_DBUS_INTERFACE_DEVICE, "State");
  raw_adapter_state = get_response<uint>(response);

  initConnections();
  requestScan();
}

void WifiManager::refreshNetworks() {
  seen_networks.clear();
  seen_ssids.clear();
  ipv4_address = get_ipv4_address();
  for (Network &network : get_networks()) {
    if (seen_ssids.count(network.ssid)) {
      continue;
    }
    seen_ssids.push_back(network.ssid);
    seen_networks.push_back(network);
  }
}

QString WifiManager::get_ipv4_address() {
  if (raw_adapter_state != NM_DEVICE_STATE_ACTIVATED) {
    return "";
  }
  QVector<QDBusObjectPath> conns = get_active_connections();
  for (auto &p : conns) {
    QString active_connection = p.path();
    QDBusInterface nm(NM_DBUS_SERVICE, active_connection, NM_DBUS_INTERFACE_PROPERTIES, bus);
    nm.setTimeout(DBUS_TIMEOUT);

    QDBusObjectPath pth = get_response<QDBusObjectPath>(nm.call("Get", NM_DBUS_INTERFACE_ACTIVE_CONNECTION, "Ip4Config"));
    QString ip4config = pth.path();

    QString type = get_response<QString>(nm.call("Get", NM_DBUS_INTERFACE_ACTIVE_CONNECTION, "Type"));

    if (type == "802-11-wireless") {
      QDBusInterface nm2(NM_DBUS_SERVICE, ip4config, NM_DBUS_INTERFACE_PROPERTIES, bus);
      nm2.setTimeout(DBUS_TIMEOUT);

      const QDBusArgument &arr = get_response<QDBusArgument>(nm2.call("Get", NM_DBUS_INTERFACE_IP4_CONFIG, "AddressData"));
      QMap<QString, QVariant> pth2;
      arr.beginArray();
      while (!arr.atEnd()) {
        arr >> pth2;
        QString ipv4 = pth2.value("address").value<QString>();
        arr.endArray();
        return ipv4;
      }
      arr.endArray();
    }
  }
  return "";
}

QList<Network> WifiManager::get_networks() {
  QList<Network> r;
  QDBusInterface nm(NM_DBUS_SERVICE, adapter, NM_DBUS_INTERFACE_DEVICE_WIRELESS, bus);
  nm.setTimeout(DBUS_TIMEOUT);

  QDBusMessage response = nm.call("GetAllAccessPoints");
  QVariant first =  response.arguments().at(0);

  QString active_ap = get_active_ap();
  const QDBusArgument &args = first.value<QDBusArgument>();
  args.beginArray();
  while (!args.atEnd()) {
    QDBusObjectPath path;
    args >> path;

    QByteArray ssid = get_property(path.path(), "Ssid");
    if (ssid.isEmpty()) {
      continue;
    }
    unsigned int strength = get_ap_strength(path.path());
    SecurityType security = getSecurityType(path.path());
    ConnectedType ctype;
    if (path.path() != active_ap) {
      ctype = ConnectedType::DISCONNECTED;
    } else {
      if (ssid == connecting_to_network) {
        ctype = ConnectedType::CONNECTING;
      } else {
        ctype = ConnectedType::CONNECTED;
      }
    }
    Network network = {path.path(), ssid, strength, ctype, security};
    r.push_back(network);
  }
  args.endArray();

  std::sort(r.begin(), r.end(), compare_by_strength);
  return r;
}

SecurityType WifiManager::getSecurityType(const QString &path) {
  int sflag = get_property(path, "Flags").toInt();
  int wpaflag = get_property(path, "WpaFlags").toInt();
  int rsnflag = get_property(path, "RsnFlags").toInt();
  int wpa_props = wpaflag | rsnflag;

  // obtained by looking at flags of networks in the office as reported by an Android phone
  const int supports_wpa = NM_802_11_AP_SEC_PAIR_WEP40 | NM_802_11_AP_SEC_PAIR_WEP104 | NM_802_11_AP_SEC_GROUP_WEP40 | NM_802_11_AP_SEC_GROUP_WEP104 | NM_802_11_AP_SEC_KEY_MGMT_PSK;

  if ((sflag == NM_802_11_AP_FLAGS_NONE) || ((sflag & NM_802_11_AP_FLAGS_WPS) && !(wpa_props & supports_wpa))) {
    return SecurityType::OPEN;
  } else if ((sflag & NM_802_11_AP_FLAGS_PRIVACY) && (wpa_props & supports_wpa) && !(wpa_props & NM_802_11_AP_SEC_KEY_MGMT_802_1X)) {
    return SecurityType::WPA;
  } else {
    LOGW("Unsupported network! sflag: %d, wpaflag: %d, rsnflag: %d", sflag, wpaflag, rsnflag);
    return SecurityType::UNSUPPORTED;
  }
}

void WifiManager::connect(const Network &n) {
  return connect(n, "", "");
}

void WifiManager::connect(const Network &n, const QString &password) {
  return connect(n, "", password);
}

void WifiManager::connect(const Network &n, const QString &username, const QString &password) {
  connecting_to_network = n.ssid;
  // disconnect();
  forgetConnection(n.ssid); //Clear all connections that may already exist to the network we are connecting
  connect(n.ssid, username, password, n.security_type);
}

void WifiManager::connect(const QByteArray &ssid, const QString &username, const QString &password, SecurityType security_type) {
  Connection connection;
  connection["connection"]["type"] = "802-11-wireless";
  connection["connection"]["uuid"] = QUuid::createUuid().toString().remove('{').remove('}');
  connection["connection"]["id"] = "openpilot connection "+QString::fromStdString(ssid.toStdString());
  connection["connection"]["autoconnect-retries"] = 0;

  connection["802-11-wireless"]["ssid"] = ssid;
  connection["802-11-wireless"]["mode"] = "infrastructure";

  if (security_type == SecurityType::WPA) {
    connection["802-11-wireless-security"]["key-mgmt"] = "wpa-psk";
    connection["802-11-wireless-security"]["auth-alg"] = "open";
    connection["802-11-wireless-security"]["psk"] = password;
  }

  connection["ipv4"]["method"] = "auto";
  connection["ipv6"]["method"] = "ignore";

  QDBusInterface nm_settings(NM_DBUS_SERVICE, NM_DBUS_PATH_SETTINGS, NM_DBUS_INTERFACE_SETTINGS, bus);
  nm_settings.setTimeout(DBUS_TIMEOUT);

  nm_settings.call("AddConnection", QVariant::fromValue(connection));
}

void WifiManager::deactivateConnection(const QString &ssid) {
  for (QDBusObjectPath active_connection_raw : get_active_connections()) {
    QString active_connection = active_connection_raw.path();
    QDBusInterface nm(NM_DBUS_SERVICE, active_connection, NM_DBUS_INTERFACE_PROPERTIES, bus);
    nm.setTimeout(DBUS_TIMEOUT);

    QDBusObjectPath pth = get_response<QDBusObjectPath>(nm.call("Get", NM_DBUS_INTERFACE_ACTIVE_CONNECTION, "SpecificObject"));
    if (pth.path() != "" && pth.path() != "/") {
      QString Ssid = get_property(pth.path(), "Ssid");
      if (Ssid == ssid) {
        QDBusInterface nm2(NM_DBUS_SERVICE, NM_DBUS_PATH, NM_DBUS_INTERFACE, bus);
        nm2.setTimeout(DBUS_TIMEOUT);
        nm2.call("DeactivateConnection", QVariant::fromValue(active_connection_raw));
      }
    }
  }
}

QVector<QDBusObjectPath> WifiManager::get_active_connections() {
  QDBusInterface nm(NM_DBUS_SERVICE, NM_DBUS_PATH, NM_DBUS_INTERFACE_PROPERTIES, bus);
  nm.setTimeout(DBUS_TIMEOUT);

  QDBusMessage response = nm.call("Get", NM_DBUS_INTERFACE, "ActiveConnections");
  const QDBusArgument &arr = get_response<QDBusArgument>(response);
  QVector<QDBusObjectPath> conns;

  QDBusObjectPath path;
  arr.beginArray();
  while (!arr.atEnd()) {
    arr >> path;
    conns.push_back(path);
  }
  arr.endArray();
  return conns;
}

bool WifiManager::isKnownConnection(const QString &ssid) {
  return !getConnectionPath(ssid).path().isEmpty();
}

void WifiManager::forgetConnection(const QString &ssid) {
  const QDBusObjectPath &path = getConnectionPath(ssid);
  if (!path.path().isEmpty()) {
    QDBusInterface nm2(NM_DBUS_SERVICE, path.path(), NM_DBUS_INTERFACE_SETTINGS_CONNECTION, bus);
    nm2.call("Delete");
  }
}

bool WifiManager::isWirelessAdapter(const QDBusObjectPath &path) {
  QDBusInterface device_props(NM_DBUS_SERVICE, path.path(), NM_DBUS_INTERFACE_PROPERTIES, bus);
  device_props.setTimeout(DBUS_TIMEOUT);
  const uint deviceType = get_response<uint>(device_props.call("Get", NM_DBUS_INTERFACE_DEVICE, "DeviceType"));
  return deviceType == NM_DEVICE_TYPE_WIFI;
}

void WifiManager::requestScan() {
  QDBusInterface nm(NM_DBUS_SERVICE, adapter, NM_DBUS_INTERFACE_DEVICE_WIRELESS, bus);
  nm.setTimeout(DBUS_TIMEOUT);
  nm.call("RequestScan",  QVariantMap());
}

uint WifiManager::get_wifi_device_state() {
  QDBusInterface device_props(NM_DBUS_SERVICE, adapter, NM_DBUS_INTERFACE_PROPERTIES, bus);
  device_props.setTimeout(DBUS_TIMEOUT);

  QDBusMessage response = device_props.call("Get", NM_DBUS_INTERFACE_DEVICE, "State");
  uint resp = get_response<uint>(response);
  return resp;
}

QString WifiManager::get_active_ap() {
  QDBusInterface device_props(NM_DBUS_SERVICE, adapter, NM_DBUS_INTERFACE_PROPERTIES, bus);
  device_props.setTimeout(DBUS_TIMEOUT);

  QDBusMessage response = device_props.call("Get", NM_DBUS_INTERFACE_DEVICE_WIRELESS, "ActiveAccessPoint");
  QDBusObjectPath r = get_response<QDBusObjectPath>(response);
  return r.path();
}

QByteArray WifiManager::get_property(const QString &network_path , const QString &property) {
  QDBusInterface device_props(NM_DBUS_SERVICE, network_path, NM_DBUS_INTERFACE_PROPERTIES, bus);
  device_props.setTimeout(DBUS_TIMEOUT);

  QDBusMessage response = device_props.call("Get", NM_DBUS_INTERFACE_ACCESS_POINT, property);
  return get_response<QByteArray>(response);
}

unsigned int WifiManager::get_ap_strength(const QString &network_path) {
  QDBusInterface device_props(NM_DBUS_SERVICE, network_path, NM_DBUS_INTERFACE_PROPERTIES, bus);
  device_props.setTimeout(DBUS_TIMEOUT);

  QDBusMessage response = device_props.call("Get", NM_DBUS_INTERFACE_ACCESS_POINT, "Strength");
  return get_response<unsigned int>(response);
}

QString WifiManager::getAdapter() {
  QDBusInterface nm(NM_DBUS_SERVICE, NM_DBUS_PATH, NM_DBUS_INTERFACE, bus);
  nm.setTimeout(DBUS_TIMEOUT);

  const QDBusReply<QList<QDBusObjectPath>> &response = nm.call("GetDevices");
  for (const QDBusObjectPath &path : response.value()) {
    if (isWirelessAdapter(path)) {
      return path.path();
    }
  }
  return "";
}

void WifiManager::stateChange(unsigned int new_state, unsigned int previous_state, unsigned int change_reason) {
  raw_adapter_state = new_state;
  if (new_state == NM_DEVICE_STATE_NEED_AUTH && change_reason == NM_DEVICE_STATE_REASON_SUPPLICANT_DISCONNECT) {
    knownConnections.remove(getConnectionPath(connecting_to_network));
    emit wrongPassword(connecting_to_network);
  } else if (new_state == NM_DEVICE_STATE_ACTIVATED) {
    connecting_to_network = "";
    if (this->isVisible()) {
      refreshNetworks();
      emit refreshSignal();
    }
  }
}

// https://developer.gnome.org/NetworkManager/stable/gdbus-org.freedesktop.NetworkManager.Device.Wireless.html
void WifiManager::propertyChange(const QString &interface, const QVariantMap &props, const QStringList &invalidated_props) {
  if (interface == NM_DBUS_INTERFACE_DEVICE_WIRELESS && props.contains("LastScan")) {
    if (this->isVisible() || firstScan) {
      refreshNetworks();
      emit refreshSignal();
      firstScan = false;
    }
  }
}

void WifiManager::deviceAdded(const QDBusObjectPath &path) {
  if (isWirelessAdapter(path) && (adapter.isEmpty() || adapter == "/")) {
    adapter = path.path();
    setup();
  }
}

void WifiManager::connectionRemoved(const QDBusObjectPath &path) {
  knownConnections.remove(path);
}

void WifiManager::newConnection(const QDBusObjectPath &path) {
  knownConnections[path] = getConnectionSsid(path);
  activateWifiConnection(knownConnections[path]);
}

void WifiManager::disconnect() {
  QString active_ap = get_active_ap();
  if (active_ap != "" && active_ap != "/") {
    deactivateConnection(get_property(active_ap, "Ssid"));
  }
}

QDBusObjectPath WifiManager::getConnectionPath(const QString &ssid) {
  for (const QString &conn_ssid : knownConnections) {
    if (ssid == conn_ssid) {
      return knownConnections.key(conn_ssid);
    }
  }
  return QDBusObjectPath();  // unknown ssid, return uninitialized path
}

QString WifiManager::getConnectionSsid(const QDBusObjectPath &path) {
  QDBusInterface nm(NM_DBUS_SERVICE, path.path(), NM_DBUS_INTERFACE_SETTINGS_CONNECTION, bus);
  nm.setTimeout(DBUS_TIMEOUT);
  const QDBusReply<Connection> result = nm.call("GetSettings");
  return result.value().value("802-11-wireless").value("ssid").toString();
}

void WifiManager::initConnections() {
  QDBusInterface nm(NM_DBUS_SERVICE, NM_DBUS_PATH_SETTINGS, NM_DBUS_INTERFACE_SETTINGS, bus);
  nm.setTimeout(DBUS_TIMEOUT);

  const QDBusReply<QList<QDBusObjectPath>> response = nm.call("ListConnections");
  for (const QDBusObjectPath &path : response.value()) {
    knownConnections[path] = getConnectionSsid(path);
  }
}

void WifiManager::activateWifiConnection(const QString &ssid) {
  const QDBusObjectPath &path = getConnectionPath(ssid);
  if (!path.path().isEmpty()) {
    connecting_to_network = ssid;
    QDBusInterface nm3(NM_DBUS_SERVICE, NM_DBUS_PATH, NM_DBUS_INTERFACE, bus);
    nm3.setTimeout(DBUS_TIMEOUT);
    nm3.call("ActivateConnection", QVariant::fromValue(path), QVariant::fromValue(QDBusObjectPath(adapter)), QVariant::fromValue(QDBusObjectPath("/")));
  }
}

// Functions for tethering
void WifiManager::addTetheringConnection() {
  Connection connection;
  connection["connection"]["id"] = "Hotspot";
  connection["connection"]["uuid"] = QUuid::createUuid().toString().remove('{').remove('}');
  connection["connection"]["type"] = "802-11-wireless";
  connection["connection"]["interface-name"] = "wlan0";
  connection["connection"]["autoconnect"] = false;

  connection["802-11-wireless"]["band"] = "bg";
  connection["802-11-wireless"]["mode"] = "ap";
  connection["802-11-wireless"]["ssid"] = tethering_ssid.toUtf8();

  connection["802-11-wireless-security"]["group"] = QStringList("ccmp");
  connection["802-11-wireless-security"]["key-mgmt"] = "wpa-psk";
  connection["802-11-wireless-security"]["pairwise"] = QStringList("ccmp");
  connection["802-11-wireless-security"]["proto"] = QStringList("rsn");
  connection["802-11-wireless-security"]["psk"] = tetheringPassword;

  connection["ipv4"]["method"] = "shared";
  QMap<QString,QVariant> address;
  address["address"] = "192.168.43.1";
  address["prefix"] = 24u;
  connection["ipv4"]["address-data"] = QVariant::fromValue(IpConfig() << address);
  connection["ipv4"]["gateway"] = "192.168.43.1";
  connection["ipv4"]["route-metric"] = 1100;
  connection["ipv6"]["method"] = "ignore";

  QDBusInterface nm_settings(NM_DBUS_SERVICE, NM_DBUS_PATH_SETTINGS, NM_DBUS_INTERFACE_SETTINGS, bus);
  nm_settings.setTimeout(DBUS_TIMEOUT);
  nm_settings.call("AddConnection", QVariant::fromValue(connection));
}

void WifiManager::enableTethering() {
  if (!isKnownConnection(tethering_ssid.toUtf8())) {
    addTetheringConnection();
  }
  activateWifiConnection(tethering_ssid.toUtf8());
}

void WifiManager::disableTethering() {
  deactivateConnection(tethering_ssid.toUtf8());
}

bool WifiManager::tetheringEnabled() {
  if (adapter != "" && adapter != "/") {
    QString active_ap = get_active_ap();
    if (active_ap != "" && active_ap != "/") {
      return get_property(active_ap, "Ssid") == tethering_ssid;
    }
  }
  return false;
}

void WifiManager::changeTetheringPassword(const QString &newPassword) {
  tetheringPassword = newPassword;
  forgetConnection(tethering_ssid.toUtf8());
  addTetheringConnection();
}
