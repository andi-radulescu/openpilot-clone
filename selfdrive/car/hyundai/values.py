# flake8: noqa

from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

# Steer torque limits
class SteerLimitParams:
  def __init__(self, CP):
    if CP.carFingerprint in [CAR.SONATA, CAR.PALISADE, CAR.SANTA_FE, CAR.VELOSTER]:
      self.STEER_MAX = 384
    else:
      self.STEER_MAX = 255
    self.STEER_DELTA_UP = 3
    self.STEER_DELTA_DOWN = 7
    self.STEER_DRIVER_ALLOWANCE = 50
    self.STEER_DRIVER_MULTIPLIER = 2
    self.STEER_DRIVER_FACTOR = 1


class CAR:
  ELANTRA = "HYUNDAI ELANTRA LIMITED ULTIMATE 2017"
  ELANTRA_GT_I30 = "HYUNDAI I30 N LINE 2019 & GT 2018 DCT"
  GENESIS_G70 = "GENESIS G70 2018"
  GENESIS_G80 = "GENESIS G80 2017"
  GENESIS_G90 = "GENESIS G90 2017"
  HYUNDAI_GENESIS = "HYUNDAI GENESIS 2015-2016"
  IONIQ = "HYUNDAI IONIQ ELECTRIC PREMIUM SE 2020"
  IONIQ_EV_LTD = "HYUNDAI IONIQ ELECTRIC LIMITED 2019"
  KIA_FORTE = "KIA FORTE E 2018"
  KIA_NIRO_EV = "KIA NIRO EV 2020"
  KIA_OPTIMA = "KIA OPTIMA SX 2019 & 2016"
  KIA_OPTIMA_H = "KIA OPTIMA HYBRID 2017 & SPORTS 2019"
  KIA_SORENTO = "KIA SORENTO GT LINE 2018"
  KIA_STINGER = "KIA STINGER GT2 2018"
  KONA = "HYUNDAI KONA 2020"
  KONA_EV = "HYUNDAI KONA ELECTRIC 2019"
  SANTA_FE = "HYUNDAI SANTA FE LIMITED 2019"
  SONATA = "HYUNDAI SONATA 2020"
  SONATA_2019 = "HYUNDAI SONATA 2019"
  PALISADE = "HYUNDAI PALISADE 2020"
  VELOSTER = "HYUNDAI VELOSTER 2019"


class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  CANCEL = 4

FINGERPRINTS = {
  CAR.ELANTRA: [{
    66: 8, 67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 897: 8, 832: 8, 899: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1170: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1314: 8, 1322: 8, 1345: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1532: 5, 2001: 8, 2003: 8, 2004: 8, 2009: 8, 2012: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.ELANTRA_GT_I30: [{
    66: 8, 67: 8, 68: 8, 127: 8, 128: 8, 129: 8, 273: 8, 274: 8, 275: 8, 339: 8, 354: 3, 356: 4, 399: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1193: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1356: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1414: 3, 1415: 8, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1952: 8, 1960: 8, 1988: 8, 2000: 8, 2001: 8, 2005: 8, 2008: 8, 2009: 8, 2013: 8, 2017: 8, 2025: 8
  },
  {
    66: 8, 67: 8, 68: 8, 127: 8, 128: 8, 129: 8, 273: 8, 274: 8, 275: 8, 339: 8, 354: 3, 356: 4, 399: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 897: 8, 899: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1356: 8, 1363: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1414: 3, 1415: 8, 1419: 8, 1440: 8, 1456: 4, 1470: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8
  },
  {
    66: 8, 67: 8, 68: 8, 127: 8, 128: 8, 129: 8, 273: 8, 274: 8, 275: 8, 339: 8, 354: 3, 356: 4, 399: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 897: 8, 899: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1356: 8, 1363: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1486: 8, 1487: 8, 1491: 8, 1960: 8, 1990: 8, 1998: 8, 2000: 8, 2001: 8, 2004: 8, 2005: 8, 2008: 8, 2009: 8, 2012: 8, 2013: 8, 2015: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.HYUNDAI_GENESIS: [{
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1024: 2, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1342: 6, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1456: 4
  },
  {
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1024: 2, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1378: 4, 1379: 8, 1384: 5, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1456: 4
  },
  {
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1268: 8, 1280: 1, 1281: 3, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1437: 8, 1456: 4
  },
  {
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1378: 4, 1379: 8, 1384: 5, 1407: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4
  },
  {
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4
  }],
  CAR.SANTA_FE: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 6, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1379: 8, 1384: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8
  },
  {
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 6, 764: 8, 809: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1183: 8, 1186: 2, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8
  },
  {
    67: 8, 68: 8, 80: 4, 160: 8, 161: 8, 272: 8, 288: 4, 339: 8, 356: 8, 357: 8, 399: 8, 544: 8, 608: 8, 672: 8, 688: 5, 704: 1, 790: 8, 809: 8, 848: 8, 880: 8, 898: 8, 900: 8, 901: 8, 904: 8, 1056: 8, 1064: 8, 1065: 8, 1072: 8, 1075: 8, 1087: 8, 1088: 8, 1151: 8, 1200: 8, 1201: 8, 1232: 4, 1264: 8, 1265: 8, 1266: 8, 1296: 8, 1306: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1348: 8, 1349: 8, 1369: 8, 1370: 8, 1371: 8, 1407: 8, 1415: 8, 1419: 8, 1440: 8, 1442: 4, 1461: 8, 1470: 8
  }],
  CAR.SONATA: [
    {67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 549: 8, 550: 8, 576: 8, 593: 8, 608: 8, 688: 6, 809: 8, 832: 8, 854: 8, 865: 8, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 908: 8, 909: 8, 912: 7, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1089: 5, 1096: 8, 1107: 5, 1108: 8, 1114: 8, 1136: 8, 1145: 8, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1170: 8, 1173: 8, 1180: 8, 1183: 8, 1184: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1268: 8, 1280: 8, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1330: 8, 1339: 8, 1342: 6, 1343: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1379: 8, 1384: 8, 1394: 8, 1407: 8, 1419: 8, 1427: 6, 1446: 8, 1456: 4, 1460: 8, 1470: 8, 1485: 8, 1504: 3, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8, 2015: 8},
  ],
  CAR.SONATA_2019: [
    {66: 8, 67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 447: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1253: 8, 1254: 8, 1255: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1314: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1397: 8, 1407: 8, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1532: 5, 2000: 8, 2001: 8, 2004: 8, 2005: 8, 2008: 8, 2009: 8, 2012: 8, 2013: 8, 2014: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8},
  ],
  CAR.KIA_OPTIMA: [{
      64: 8, 66: 8, 67: 8, 68: 8, 127: 8, 128: 8, 129: 8, 273: 8, 274: 8, 275: 8, 339: 8, 354: 3, 356: 4, 399: 8, 447: 8, 512: 6, 544: 8, 558: 8, 593: 8, 608: 8, 640: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 6, 909: 8, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1186: 2, 1191: 2, 1253: 8, 1254: 8, 1255: 8, 1265: 4, 1268: 8, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1356: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1414: 3, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1492: 8, 1530: 8, 1532: 5, 1792: 8, 1872: 8, 1937: 8, 1953: 8, 1968: 8, 1988: 8, 1996: 8, 2000: 8, 2001: 8, 2004: 8, 2008: 8, 2009: 8, 2012: 8, 2015: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.KIA_SORENTO: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1384: 8, 1407: 8, 1411: 8, 1419: 8, 1425: 2, 1427: 6, 1444: 8, 1456: 4, 1470: 8, 1489: 1
  }],
  CAR.KIA_STINGER: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1379: 8, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8
  }],
  CAR.GENESIS_G70: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832:8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1168: 7, 1170: 8, 1173:8, 1184: 8, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1379: 8, 1384: 8, 1407: 8, 1419:8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8, 2015: 8
  }],
  CAR.GENESIS_G80: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1024: 2, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8
  },
  {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 546: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1437: 8, 1456: 4, 1470: 8
  },
  {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 8, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1193: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4, 1470: 8
  }],
  CAR.GENESIS_G90: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8, 1988: 8, 2000: 8, 2003: 8, 2004: 8, 2005: 8, 2008: 8, 2011: 8, 2012: 8, 2013: 8
  }],
  CAR.IONIQ_EV_LTD: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 7, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1168: 7, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1425: 2, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1507: 8, 1535: 8
  }],
  CAR.IONIQ: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 524: 8, 544: 7, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1164: 8, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1379: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2005: 8, 2008: 8, 2012: 8, 2013: 8
  },
  {
    68:8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 524: 8, 544: 8, 576:8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1164: 8, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1379: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1473: 8, 1476: 8, 1507: 8, 1535: 8, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2005: 8, 2008: 8, 2012: 8, 2013: 8
  }],
  CAR.KONA: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 354: 3, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832 : 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1170: 8, 1173: 8, 1186: 2, 1191: 2, 1193: 8, 1265: 4,1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1378: 8, 1384: 8, 1394: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 1996: 8, 2000: 8, 2001: 8, 2004: 8, 2008: 8, 2009: 8, 2012: 8
  }],
  CAR.KONA_EV: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 549: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1307: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1378: 4, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8, 1157: 4, 1193: 8, 1379: 8, 1988: 8, 1996: 8
  }],
  CAR.KIA_NIRO_EV: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 516: 8, 544: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1193: 8, 1225: 8, 1260: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8, 1990: 8, 1998: 8, 1996: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8, 2015: 8
  }],
  CAR.KIA_FORTE: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1078: 4, 1107: 5, 1136: 8, 1156: 8, 1170: 8, 1173: 8, 1191: 2, 1225: 8, 1265: 4, 1280: 4, 1287: 4, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1384: 8, 1394: 8, 1407: 8, 1427: 6, 1456: 4, 1470: 8
  }],
  CAR.KIA_OPTIMA_H: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1151: 6, 1168: 7, 1173: 8, 1236: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  },
  {
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 909: 8, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1151: 6, 1168: 7, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1407: 8, 1419: 8, 1420: 8, 1425: 2, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  }],
  CAR.PALISADE: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 547: 8, 548: 8, 549: 8, 576: 8, 593: 8, 608: 8, 688: 6, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1123: 8, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1280: 8, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2005: 8, 2008: 8, 2012: 8
  }],
  CAR.VELOSTER: [{
    64: 8, 66: 8, 67: 8, 68: 8, 127: 8, 128: 8, 129: 8, 273: 8, 274: 8, 275: 8, 339: 8, 354: 3, 356: 4, 399: 8, 512: 6, 544: 8, 558: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1170: 8, 1181: 5, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1356: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1378: 4, 1407: 8, 1414: 3, 1415: 8, 1419: 8, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1532: 5, 1872: 8, 1988: 8, 1996: 8, 2000: 8, 2001: 8, 2004: 8, 2008: 8, 2009: 8, 2012: 8, 2015: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }]
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [832, 1156, 1191, 1342]
}

# Don't use these fingerprints for fingerprinting, they are still used for ECU detection
IGNORED_FINGERPRINTS = [CAR.VELOSTER, CAR.GENESIS_G70, CAR.KONA]

FW_VERSIONS = {
  CAR.SONATA: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00DN8_ SCC FHCUP      1.00 1.01 99110-L1000         ',
      b'\xf1\x00DN8_ SCC FHCUP      1.00 1.00 99110-L0000         ',
      b'\xf1\x00DN8_ SCC F-CU-      1.00 1.00 99110-L0000         ',
    ],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x00DN ESC \x01 102\x19\x04\x13 58910-L1300\xf1\xa01.02',
      b'\xf1\x8758910-L0100\xf1\x00DN ESC \x06 104\x19\x08\x01 58910-L0100\xf1\xa01.04',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'HM6M2_0a0_BD0',
      b'\xf1\x87391162M003\xf1\xa0000F',
      b'\xf1\x87391162M003\xf1\xa00240',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x8756310-L1010\xf1\x00DN8 MDPS C 1.00 1.03 56310-L1010 4DNDC103\xf1\xa01.03',
      b'\xf1\x8756310L0010\x00\xf1\x00DN8 MDPS C 1.00 1.01 56310L0010\x00 4DNAC101\xf1\xa01.01',
      b'\xf1\x8756310-L0010\xf1\x00DN8 MDPS C 1.00 1.01 56310-L0010 4DNAC101\xf1\xa01.01',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00DN8 MFC  AT KOR LHD 1.00 1.02 99211-L1000 190422',
      b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.00 99211-L0000 190716',
      b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.01 99211-L0000 191016',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x00HT6TA260BLHT6TA800A1TDN8C20KS4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x00bcsh8p54  U903\x00\x00\x00\x00\x00\x00SDN8T16NB0z{\xd4v',
    ],
  },
  CAR.SANTA_FE: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00TM__ SCC F-CUP      1.00 1.02 99110-S2000         \xf1\xa01.02'],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00TM ESC \x02 100\x18\x030 58910-S2600\xf1\xa01.00',],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81606EA051\x00\x00\x00\x00\x00\x00\x00\x00'],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00TM  MFC  AT USA LHD 1.00 1.00 99211-S2000 180409'],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x87SBJWAA6562474GG0ffvgeTeFx\x88\x97\x88ww\x87www\x87w\x84o\xfa\xff\x87fO\xff\xc2 \xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS1\x00\x00\x00\x00'],
  },
  CAR.KIA_STINGER: {
    (Ecu.fwdRadar, 0x7d0, None): [ b'\xf1\x00CK__ SCC F_CUP      1.00 1.01 96400-J5100         \xf1\xa01.01'],
    (Ecu.engine, 0x7e0, None): [ b'\xf1\x81640E0051\x00\x00\x00\x00\x00\x00\x00\x00',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00CK  MDPS R 1.00 1.04 57700-J5420 4C4VL104'],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00CK  MFC  AT USA LHD 1.00 1.03 95740-J5000 170822'],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x87VDHLG17118862DK2\x8awWwgu\x96wVfUVwv\x97xWvfvUTGTx\x87o\xff\xc9\xed\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
      b'\xf1\x87VDHLG17000192DK2xdFffT\xa5VUD$DwT\x86wveVeeD&T\x99\xba\x8f\xff\xcc\x99\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
    ],
  },
  CAR.KIA_OPTIMA_H: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00DEhe SCC H-CUP      1.01 1.02 96400-G5100         ',],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x816H6F4051\x00\x00\x00\x00\x00\x00\x00\x00',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00DE  MDPS C 1.00 1.09 56310G5301\x00 4DEHC109',],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00DEP MFC  AT USA LHD 1.00 1.01 95740-G5010 170424',],
    (Ecu.transmission, 0x7e1, None): [b"\xf1\x816U3J2051\x00\x00\xf1\x006U3H0_C2\x00\x006U3J2051\x00\x00PDE0G16NS2\xf4'\\\x91",],
  },
  CAR.PALISADE: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00LX2_ SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',
      b'\xf1\x00LX2 SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',
    ],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x00LX ESC \v 102\x19\x05\a 58910-S8330\xf1\xa01.02',
      b'\xf1\x00LX ESC \v 103\x19\t\x10 58910-S8360\xf1\xa01.03',
      b'\xf1\x00LX ESC \x01 103\x19\t\x10 58910-S8360\xf1\xa01.03',
      b'\xf1\x00LX ESC \x0b 102\x19\x05\x07 58910-S8330',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x81640J0051\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x81640K0051\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00LX2 MDPS C 1.00 1.03 56310-S8020 4LXDC103',],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.03 99211-S8100 190125',
      b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.05 99211-S8100 190909',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x87LBLUFN650868KF36\xa9\x98\x89\x88\xa8\x88\x88\x88h\x99\xa6\x89fw\x86gw\x88\x97x\xaa\x7f\xf6\xff\xbb\xbb\x8f\xff+\x82\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8',
      b'\xf1\x87LDKVBN424201KF26\xba\xaa\x9a\xa9\x99\x99\x89\x98\x89\x99\xa8\x99\x88\x99\x98\x89\x88\x99\xa8\x89v\x7f\xf7\xffwf_\xffq\xa6\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
      b'\xf1\x87LDLVBN560098KF26\x86fff\x87vgfg\x88\x96xfw\x86gfw\x86g\x95\xf6\xffeU_\xff\x92c\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
    ],
  },
  CAR.VELOSTER: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00JS__ SCC H-CUP      1.00 1.02 95650-J3200         ', ],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00\x00\x00\x00\x00\x00\x00', ],
    (Ecu.engine, 0x7e0, None): [b'\x01TJS-JNU06F200H0A', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00JSL MDPS C 1.00 1.03 56340-J3000 8308', ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00JS  LKAS AT USA LHD 1.00 1.02 95740-J3000 K32', ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJS0T16NS1\xba\x02\xb8\x80',
      b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJS0T16NS1\x00\x00\x00\x00',
    ],
  },
  CAR.GENESIS_G70: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00IK__ SCC F-CUP      1.00 1.02 96400-G9100         \xf1\xa01.02', ],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00\x00\x00\x00\x00\x00\x00', ],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81640F0051\x00\x00\x00\x00\x00\x00\x00\x00', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00IK  MDPS R 1.00 1.06 57700-G9420 4I4VL106', ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00IK  MFC  AT USA LHD 1.00 1.01 95740-G9000 170920', ],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x87VDJLT17895112DN4\x88fVf\x99\x88\x88\x88\x87fVe\x88vhwwUFU\x97eFex\x99\xff\xb7\x82\xf1\x81E25\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E25\x00\x00\x00\x00\x00\x00\x00SIK0T33NB2\x11\x1am\xda', ],
  },
  CAR.KONA: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00OS__ SCC F-CUP      1.00 1.00 95655-J9200         \xf1\xa01.00', ],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x816V5RAK00018.ELF\xf1\x00\x00\x00\x00\x00\x00\x00\xf1\xa01.05', ],
    (Ecu.engine, 0x7e0, None): [b'"\x01TOS-0NU06F301J02', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00OS  MDPS C 1.00 1.05 56310J9030\x00 4OSDC105', ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00OS9 LKAS AT USA LHD 1.00 1.00 95740-J9300 g21', ],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2VE051\x00\x00\xf1\x006U2V0_C2\x00\x006U2VE051\x00\x00DOS4T16NS3\x00\x00\x00\x00', ],
  },
  CAR.KIA_NIRO_EV: {
    (Ecu.fwdRadar, 0x7D0, None): [
      b'\xf1\x00DEev SCC F-CUP      1.00 1.03 96400-Q4100         \xf1\xa01.03',
      b'\xf1\x00DEev SCC F-CUP      1.00 1.00 99110-Q4000         \xf1\xa01.00',      
    ],
    (Ecu.esp, 0x7D1, None): [
      b'\xf1\xa01.06',
      b'\xf1\xa01.07',
    ],
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4000\x00 4DEEC105',
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4100\x00 4DEEC105',
    ],
    (Ecu.fwdCamera, 0x7C4, None): [
      b'\xf1\x00DEE MFC  AT USA LHD 1.00 1.03 95740-Q4000 180821',
      b'\xf1\x00DEE MFC  AT EUR LHD 1.00 1.00 99211-Q4000 191211',
    ],
  },
  CAR.KIA_OPTIMA: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00JF__ SCC F-CUP      1.00 1.00 96400-D4110         '],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00JF ESC \v 11 \x18\x030 58920-D5180',],
    (Ecu.engine, 0x7e0, None): [b'\x01TJFAJNU06F201H03'],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00JFA LKAS AT USA LHD 1.00 1.02 95895-D5000 h31'],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJF0T16NL0\t\xd2GW'],
  }
}

CHECKSUM = {
  "crc8": [CAR.SANTA_FE, CAR.SONATA, CAR.PALISADE],
  "6B": [CAR.KIA_SORENTO, CAR.HYUNDAI_GENESIS],
}

FEATURES = {
  # which message has the gear
  "use_cluster_gears": set([CAR.ELANTRA, CAR.ELANTRA_GT_I30, CAR.KONA]),
  "use_tcu_gears": set([CAR.KIA_OPTIMA, CAR.SONATA_2019, CAR.VELOSTER]),
  "use_elect_gears": set([CAR.KIA_NIRO_EV, CAR.KIA_OPTIMA_H, CAR.IONIQ_EV_LTD, CAR.KONA_EV, CAR.IONIQ]),

  # these cars use the FCA11 message for the AEB and FCW signals, all others use SCC12
  "use_fca": set([CAR.SONATA, CAR.ELANTRA, CAR.ELANTRA_GT_I30, CAR.KIA_STINGER, CAR.IONIQ, CAR.KONA_EV, CAR.KIA_FORTE, CAR.KIA_NIRO_EV, CAR.PALISADE, CAR.GENESIS_G70, CAR.KONA]),

  "use_bsm": set([CAR.SONATA, CAR.PALISADE, CAR.HYUNDAI_GENESIS, CAR.GENESIS_G70, CAR.GENESIS_G80, CAR.GENESIS_G90, CAR.KONA]),
}

EV_HYBRID = set([CAR.IONIQ_EV_LTD, CAR.IONIQ, CAR.KONA_EV, CAR.KIA_NIRO_EV])

DBC = {
  CAR.ELANTRA: dbc_dict('hyundai_kia_generic', None),
  CAR.ELANTRA_GT_I30: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G70: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G80: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G90: dbc_dict('hyundai_kia_generic', None),
  CAR.HYUNDAI_GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV_LTD: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_FORTE: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_OPTIMA: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_OPTIMA_H: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_SORENTO: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_STINGER: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_2019: dbc_dict('hyundai_kia_generic', None),
  CAR.PALISADE: dbc_dict('hyundai_kia_generic', None),
  CAR.VELOSTER: dbc_dict('hyundai_kia_generic', None),
}

STEER_THRESHOLD = 150
