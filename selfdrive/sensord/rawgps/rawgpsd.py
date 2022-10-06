#!/usr/bin/env python3
import os
import sys
import signal
import itertools
import math
import time
import subprocess
from typing import NoReturn
from struct import unpack_from, calcsize, pack

from cereal import log
import cereal.messaging as messaging
from laika.gps_time import GPSTime
from system.swaglog import cloudlog
from selfdrive.sensord.rawgps.modemdiag import ModemDiag, DIAG_LOG_F, setup_logs, send_recv
from selfdrive.sensord.rawgps.structs import (dict_unpacker, position_report,
                                              gps_measurement_report, gps_measurement_report_sv,
                                              glonass_measurement_report, glonass_measurement_report_sv,
                                              oemdre_measurement_report, oemdre_measurement_report_sv,
                                              LOG_GNSS_GPS_MEASUREMENT_REPORT, LOG_GNSS_GLONASS_MEASUREMENT_REPORT,
                                              LOG_GNSS_POSITION_REPORT, LOG_GNSS_OEMDRE_MEASUREMENT_REPORT)

DEBUG = int(os.getenv("DEBUG", "0"))==1

LOG_TYPES = [
  LOG_GNSS_GPS_MEASUREMENT_REPORT,
  LOG_GNSS_GLONASS_MEASUREMENT_REPORT,
  LOG_GNSS_OEMDRE_MEASUREMENT_REPORT,
  LOG_GNSS_POSITION_REPORT,
]


miscStatusFields = {
  "multipathEstimateIsValid": 0,
  "directionIsValid": 1,
}

measurementStatusFields = {
  "subMillisecondIsValid": 0,
  "subBitTimeIsKnown": 1,
  "satelliteTimeIsKnown": 2,
  "bitEdgeConfirmedFromSignal": 3,
  "measuredVelocity": 4,
  "fineOrCoarseVelocity": 5,
  "lockPointValid": 6,
  "lockPointPositive": 7,

  "lastUpdateFromDifference": 9,
  "lastUpdateFromVelocityDifference": 10,
  "strongIndicationOfCrossCorelation": 11,
  "tentativeMeasurement": 12,
  "measurementNotUsable": 13,
  "sirCheckIsNeeded": 14,
  "probationMode": 15,

  "multipathIndicator": 24,
  "imdJammingIndicator": 25,
  "lteB13TxJammingIndicator": 26,
  "freshMeasurementIndicator": 27,
}

measurementStatusGPSFields = {
  "gpsRoundRobinRxDiversity": 18,
  "gpsRxDiversity": 19,
  "gpsLowBandwidthRxDiversityCombined": 20,
  "gpsHighBandwidthNu4": 21,
  "gpsHighBandwidthNu8": 22,
  "gpsHighBandwidthUniform": 23,
}

measurementStatusGlonassFields = {
  "glonassMeanderBitEdgeValid": 16,
  "glonassTimeMarkValid": 17
}


def try_setup_logs(diag, log_types):
  for _ in range(5):
    try:
      setup_logs(diag, log_types)
      break
    except Exception:
      cloudlog.exception("setup logs failed, trying again")
  else:
    raise Exception(f"setup logs failed, {log_types=}")

def mmcli(cmd: str) -> None:
  for _ in range(5):
    try:
      subprocess.check_call(f"mmcli -m 0 {cmd}", shell=True)
      break
    except subprocess.CalledProcessError:
      cloudlog.exception("rawgps.mmcli_command_failed")
  else:
    raise Exception(f"failed to execute mmcli command {cmd=}")

def setup_quectel(diag: ModemDiag):
  # enable OEMDRE in the NV
  # TODO: it has to reboot for this to take effect
  DIAG_NV_READ_F = 38
  DIAG_NV_WRITE_F = 39
  NV_GNSS_OEM_FEATURE_MASK = 7165
  send_recv(diag, DIAG_NV_WRITE_F, pack('<HI', NV_GNSS_OEM_FEATURE_MASK, 1))
  send_recv(diag, DIAG_NV_READ_F, pack('<H', NV_GNSS_OEM_FEATURE_MASK))

  setup_logs(diag, LOG_TYPES)

  # disable DPO power savings for more accuracy
  mmcli("--command='AT+QGPSCFG=\"dpoenable\",0'")
  # don't automatically turn on GNSS on powerup
  mmcli("--command='AT+QGPSCFG=\"autogps\",0'")
  mmcli("--location-enable-gps-raw --location-enable-gps-nmea")

  # enable OEMDRE mode
  DIAG_SUBSYS_CMD_F = 75
  DIAG_SUBSYS_GPS = 13
  CGPS_DIAG_PDAPI_CMD = 0x64
  CGPS_OEM_CONTROL = 202
  GPSDIAG_OEMFEATURE_DRE = 1
  GPSDIAG_OEM_DRE_ON = 1

  # gpsdiag_OemControlReqType
  send_recv(diag, DIAG_SUBSYS_CMD_F, pack('<BHBBIIII',
    DIAG_SUBSYS_GPS,           # Subsystem Id
    CGPS_DIAG_PDAPI_CMD,       # Subsystem Command Code
    CGPS_OEM_CONTROL,          # CGPS Command Code
    0,                         # Version
    GPSDIAG_OEMFEATURE_DRE,
    GPSDIAG_OEM_DRE_ON,
    0,0
  ))

def teardown_quectel(diag):
  mmcli("--location-disable-gps-raw --location-disable-gps-nmea")
  try_setup_logs(diag, [])


def main() -> NoReturn:
  unpack_gps_meas, size_gps_meas = dict_unpacker(gps_measurement_report, True)
  unpack_gps_meas_sv, size_gps_meas_sv = dict_unpacker(gps_measurement_report_sv, True)

  unpack_glonass_meas, size_glonass_meas = dict_unpacker(glonass_measurement_report, True)
  unpack_glonass_meas_sv, size_glonass_meas_sv = dict_unpacker(glonass_measurement_report_sv, True)

  unpack_oemdre_meas, size_oemdre_meas = dict_unpacker(oemdre_measurement_report, True)
  unpack_oemdre_meas_sv, size_oemdre_meas_sv = dict_unpacker(oemdre_measurement_report_sv, True)

  unpack_position, _ = dict_unpacker(position_report)

  # wait for ModemManager to come up
  cloudlog.warning("waiting for modem to come up")
  while True:
    ret = subprocess.call("mmcli -m 0 --location-status", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    if ret == 0:
      break
    time.sleep(0.1)

  # connect to modem
  diag = ModemDiag()

  def cleanup(sig, frame):
    cloudlog.warning(f"caught sig {sig}, disabling quectel gps")
    teardown_quectel(diag)
    cloudlog.warning("quectel cleanup done")
    sys.exit(0)
  signal.signal(signal.SIGINT, cleanup)
  signal.signal(signal.SIGTERM, cleanup)

  setup_quectel(diag)
  cloudlog.warning("quectel setup done")

  pm = messaging.PubMaster(['qcomGnss', 'gpsLocation'])

  while 1:
    opcode, payload = diag.recv()
    assert opcode == DIAG_LOG_F

    (pending_msgs, log_outer_length), inner_log_packet = unpack_from('<BH', payload), payload[calcsize('<BH'):]
    if pending_msgs > 0:
      cloudlog.debug("have %d pending messages" % pending_msgs)
    assert log_outer_length == len(inner_log_packet)

    (log_inner_length, log_type, log_time), log_payload = unpack_from('<HHQ', inner_log_packet), inner_log_packet[calcsize('<HHQ'):]
    assert log_inner_length == len(inner_log_packet)

    if log_type not in LOG_TYPES:
      continue

    if DEBUG:
      print("%.4f: got log: %x len %d" % (time.time(), log_type, len(log_payload)))

    if log_type == LOG_GNSS_OEMDRE_MEASUREMENT_REPORT:
      msg = messaging.new_message('qcomGnss')

      gnss = msg.qcomGnss
      gnss.logTs = log_time
      gnss.init('drMeasurementReport')
      report = gnss.drMeasurementReport

      dat = unpack_oemdre_meas(log_payload)
      for k,v in dat.items():
        if k in ["gpsTimeBias", "gpsClockTimeUncertainty"]:
          k += "Ms"
        if k == "version":
          assert v == 2
        elif k == "svCount" or k.startswith("cdmaClockInfo["):
          # TODO: should we save cdmaClockInfo?
          pass
        elif k == "systemRtcValid":
          setattr(report, k, bool(v))
        else:
          setattr(report, k, v)

      report.init('sv', dat['svCount'])
      sats = log_payload[size_oemdre_meas:]
      for i in range(dat['svCount']):
        sat = unpack_oemdre_meas_sv(sats[size_oemdre_meas_sv*i:size_oemdre_meas_sv*(i+1)])
        sv = report.sv[i]
        sv.init('measurementStatus')
        for k,v in sat.items():
          if k in ["unkn", "measurementStatus2"]:
            pass
          elif k == "multipathEstimateValid":
            sv.measurementStatus.multipathEstimateIsValid = bool(v)
          elif k == "directionValid":
            sv.measurementStatus.directionIsValid = bool(v)
          elif k == "goodParity":
            setattr(sv, k, bool(v))
          elif k == "measurementStatus":
            for kk,vv in measurementStatusFields.items():
              setattr(sv.measurementStatus, kk, bool(v & (1<<vv)))
          else:
            setattr(sv, k, v)
      pm.send('qcomGnss', msg)
    elif log_type == LOG_GNSS_POSITION_REPORT:
      report = unpack_position(log_payload)
      if report["u_PosSource"] != 2:
        continue
      vNED = [report["q_FltVelEnuMps[1]"], report["q_FltVelEnuMps[0]"], -report["q_FltVelEnuMps[2]"]]
      vNEDsigma = [report["q_FltVelSigmaMps[1]"], report["q_FltVelSigmaMps[0]"], -report["q_FltVelSigmaMps[2]"]]

      msg = messaging.new_message('gpsLocation')
      gps = msg.gpsLocation
      gps.flags = 1
      gps.latitude = report["t_DblFinalPosLatLon[0]"] * 180/math.pi
      gps.longitude = report["t_DblFinalPosLatLon[1]"] * 180/math.pi
      gps.altitude = report["q_FltFinalPosAlt"]
      gps.speed = math.sqrt(sum([x**2 for x in vNED]))
      gps.bearingDeg = report["q_FltHeadingRad"] * 180/math.pi
      gps.unixTimestampMillis = GPSTime(report['w_GpsWeekNumber'],
                                        1e-3*report['q_GpsFixTimeMs']).as_unix_timestamp()*1e3
      gps.source = log.GpsLocationData.SensorSource.qcomdiag
      gps.vNED = vNED
      gps.verticalAccuracy = report["q_FltVdop"]
      gps.bearingAccuracyDeg = report["q_FltHeadingUncRad"] * 180/math.pi
      gps.speedAccuracy = math.sqrt(sum([x**2 for x in vNEDsigma]))

      pm.send('gpsLocation', msg)

    if log_type in [LOG_GNSS_GPS_MEASUREMENT_REPORT, LOG_GNSS_GLONASS_MEASUREMENT_REPORT]:
      msg = messaging.new_message('qcomGnss')

      gnss = msg.qcomGnss
      gnss.logTs = log_time
      gnss.init('measurementReport')
      report = gnss.measurementReport

      if log_type == LOG_GNSS_GPS_MEASUREMENT_REPORT:
        dat = unpack_gps_meas(log_payload)
        sats = log_payload[size_gps_meas:]
        unpack_meas_sv, size_meas_sv = unpack_gps_meas_sv, size_gps_meas_sv
        report.source = 0  # gps
        measurement_status_fields = (measurementStatusFields.items(), measurementStatusGPSFields.items())
      elif log_type == LOG_GNSS_GLONASS_MEASUREMENT_REPORT:
        dat = unpack_glonass_meas(log_payload)
        sats = log_payload[size_glonass_meas:]
        unpack_meas_sv, size_meas_sv = unpack_glonass_meas_sv, size_glonass_meas_sv
        report.source = 1  # glonass
        measurement_status_fields = (measurementStatusFields.items(), measurementStatusGlonassFields.items())
      else:
        assert False

      for k,v in dat.items():
        if k == "version":
          assert v == 0
        elif k == "week":
          report.gpsWeek = v
        elif k == "svCount":
          pass
        else:
          setattr(report, k, v)
      report.init('sv', dat['svCount'])
      if dat['svCount'] > 0:
        assert len(sats)//dat['svCount'] == size_meas_sv
        for i in range(dat['svCount']):
          sv = report.sv[i]
          sv.init('measurementStatus')
          sat = unpack_meas_sv(sats[size_meas_sv*i:size_meas_sv*(i+1)])
          for k,v in sat.items():
            if k == "parityErrorCount":
              sv.gpsParityErrorCount = v
            elif k == "frequencyIndex":
              sv.glonassFrequencyIndex = v
            elif k == "hemmingErrorCount":
              sv.glonassHemmingErrorCount = v
            elif k == "measurementStatus":
              for kk,vv in itertools.chain(*measurement_status_fields):
                setattr(sv.measurementStatus, kk, bool(v & (1<<vv)))
            elif k == "miscStatus":
              for kk,vv in miscStatusFields.items():
                setattr(sv.measurementStatus, kk, bool(v & (1<<vv)))
            elif k == "pad":
              pass
            else:
              setattr(sv, k, v)

      pm.send('qcomGnss', msg)

if __name__ == "__main__":
  main()
