# ruff: noqa: E501
from openpilot.selfdrive.car.gm.values import CAR

# Trailblazer also matches as a SILVERADO, TODO: split with fw versions
# FIXME: There are Equinox users with different message lengths, specifically 304 and 320


FINGERPRINTS = {
  CAR.HOLDEN_ASTRA: [{
    190: 8, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 8, 241: 6, 249: 8, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 328: 1, 352: 5, 381: 6, 384: 4, 386: 8, 388: 8, 393: 8, 398: 8, 401: 8, 413: 8, 417: 8, 419: 8, 422: 1, 426: 7, 431: 8, 442: 8, 451: 8, 452: 8, 453: 8, 455: 7, 456: 8, 458: 5, 479: 8, 481: 7, 485: 8, 489: 8, 497: 8, 499: 3, 500: 8, 501: 8, 508: 8, 528: 5, 532: 6, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 567: 5, 647: 5, 707: 8, 715: 8, 723: 8, 753: 5, 761: 7, 806: 1, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 961: 8, 969: 8, 977: 8, 979: 8, 985: 5, 1001: 8, 1009: 8, 1011: 6, 1017: 8, 1019: 3, 1020: 8, 1105: 6, 1217: 8, 1221: 5, 1225: 8, 1233: 8, 1249: 8, 1257: 6, 1259: 8, 1261: 7, 1263: 4, 1265: 8, 1267: 8, 1280: 4, 1300: 8, 1328: 4, 1417: 8, 1906: 7, 1907: 7, 1908: 7, 1912: 7, 1919: 7
  }],
  CAR.CHEVROLET_VOLT: [{
    170: 8, 171: 8, 189: 7, 190: 6, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 2, 241: 6, 288: 5, 289: 8, 298: 8, 304: 1, 308: 4, 309: 8, 311: 8, 313: 8, 320: 3, 328: 1, 352: 5, 381: 6, 384: 4, 386: 8, 388: 8, 389: 2, 390: 7, 417: 7, 419: 1, 426: 7, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 479: 3, 481: 7, 485: 8, 489: 8, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 508: 8, 528: 4, 532: 6, 546: 7, 550: 8, 554: 3, 558: 8, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 566: 5, 567: 3, 568: 1, 573: 1, 577: 8, 647: 3, 707: 8, 711: 6, 715: 8, 761: 7, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 961: 8, 969: 8, 977: 8, 979: 7, 988: 6, 989: 8, 995: 7, 1001: 8, 1005: 6, 1009: 8, 1017: 8, 1019: 2, 1020: 8, 1105: 6, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1249: 8, 1257: 6, 1265: 8, 1267: 1, 1273: 3, 1275: 3, 1280: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1417: 8, 1601: 8, 1905: 7, 1906: 7, 1907: 7, 1910: 7, 1912: 7, 1922: 7, 1927: 7, 1928: 7, 2016: 8, 2020: 8, 2024: 8, 2028: 8
  },
  {
    170: 8, 171: 8, 189: 7, 190: 6, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 2, 241: 6, 288: 5, 298: 8, 304: 1, 308: 4, 309: 8, 311: 8, 313: 8, 320: 3, 328: 1, 352: 5, 381: 6, 384: 4, 386: 8, 388: 8, 389: 2, 390: 7, 417: 7, 419: 1, 426: 7, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 479: 3, 481: 7, 485: 8, 489: 8, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 508: 8, 528: 4, 532: 6, 546: 7, 550: 8, 554: 3, 558: 8, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 566: 5, 567: 3, 568: 1, 573: 1, 577: 8, 578: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 715: 8, 717: 5, 761: 7, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 869: 4, 880: 6, 961: 8, 967: 4, 969: 8, 977: 8, 979: 7, 988: 6, 989: 8, 995: 7, 1001: 8, 1005: 6, 1009: 8, 1017: 8, 1019: 2, 1020: 8, 1033: 7, 1034: 7, 1105: 6, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1249: 8, 1257: 6, 1265: 8, 1267: 1, 1273: 3, 1275: 3, 1280: 4, 1296: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1417: 8, 1516: 8, 1601: 8, 1618: 8, 1905: 7, 1906: 7, 1907: 7, 1910: 7, 1912: 7, 1922: 7, 1927: 7, 1930: 7, 2016: 8, 2018: 8, 2020: 8, 2024: 8, 2028: 8
  },
  {
    170: 8, 171: 8, 189: 7, 190: 6, 192: 5, 193: 8, 197: 8, 199: 4, 201: 6, 209: 7, 211: 2, 241: 6, 288: 5, 289: 1, 290: 1, 298: 2, 304: 1, 308: 4, 309: 8, 311: 8, 313: 8, 320: 3, 328: 1, 352: 5, 368: 8, 381: 2, 384: 8, 386: 5, 388: 8, 389: 2, 390: 7, 417: 7, 419: 1, 426: 7, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 458: 8, 479: 3, 481: 7, 485: 8, 489: 5, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 3, 508: 8, 512: 3, 528: 4, 530: 8, 532: 6, 537: 5, 539: 8, 542: 7, 546: 7, 550: 8, 554: 3, 558: 8, 560: 6, 562: 4, 563: 5, 564: 5, 565: 5, 566: 5, 567: 3, 568: 1, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 761: 7, 810: 8, 821: 4, 823: 7, 832: 8, 840: 5, 842: 5, 844: 8, 853: 8, 866: 4, 961: 8, 967: 4, 969: 8, 977: 8, 979: 7, 988: 6, 989: 8, 995: 7, 1001: 5, 1003: 5, 1005: 6, 1009: 8, 1017: 8, 1019: 2, 1020: 8, 1033: 7, 1034: 7, 1105: 6, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1249: 8, 1257: 6, 1265: 8, 1267: 1, 1273: 3, 1275: 3, 1280: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1417: 8, 1905: 7, 1906: 7, 1907: 7, 1910: 7, 1912: 7, 1922: 7, 1927: 7
  }],
  CAR.BUICK_LACROSSE: [{
    190: 6, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 2, 241: 6, 249: 8, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 353: 3, 381: 6, 386: 8, 388: 8, 393: 7, 398: 8, 407: 7, 413: 8, 417: 7, 419: 1, 422: 4, 426: 7, 431: 8, 442: 8, 451: 8, 452: 8, 453: 6, 455: 7, 456: 8, 463: 3, 479: 3, 481: 7, 485: 8, 487: 8, 489: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 1, 508: 8, 510: 8, 528: 5, 532: 6, 534: 2, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 567: 5, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 5, 707: 8, 753: 5, 761: 7, 801: 8, 804: 3, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 872: 1, 882: 8, 890: 1, 892: 2, 893: 1, 894: 1, 961: 8, 967: 4, 969: 8, 977: 8, 979: 8, 985: 5, 1001: 8, 1005: 6, 1009: 8, 1011: 6, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1105: 6, 1217: 8, 1221: 5, 1223: 2, 1225: 7, 1233: 8, 1243: 3, 1249: 8, 1257: 6, 1259: 8, 1261: 7, 1263: 4, 1265: 8, 1267: 1, 1280: 4, 1300: 8, 1322: 6, 1328: 4, 1417: 8, 1609: 8, 1613: 8, 1649: 8, 1792: 8, 1798: 8, 1824: 8, 1825: 8, 1840: 8, 1842: 8, 1858: 8, 1860: 8, 1863: 8, 1872: 8, 1875: 8, 1882: 8, 1888: 8, 1889: 8, 1892: 8, 1904: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1914: 7, 1916: 7, 1918: 7, 1919: 7, 1937: 8, 1953: 8, 1968: 8, 2001: 8, 2017: 8, 2018: 8, 2020: 8, 2026: 8
  }],
  CAR.BUICK_REGAL: [{
    190: 8, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 8, 241: 6, 249: 8, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 381: 6, 384: 4, 386: 8, 388: 8, 393: 7, 398: 8, 407: 7, 413: 8, 417: 8, 419: 8, 422: 4, 426: 8, 431: 8, 442: 8, 451: 8, 452: 8, 453: 8, 455: 7, 456: 8, 463: 3, 479: 8, 481: 7, 485: 8, 487: 8, 489: 8, 495: 8, 497: 8, 499: 3, 500: 8, 501: 8, 508: 8, 528: 5, 532: 6, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 567: 5, 569: 3, 573: 1, 577: 8, 578: 8, 579: 8, 587: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 715: 8, 717: 5, 753: 5, 761: 7, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 869: 4, 880: 6, 882: 8, 884: 8, 890: 1, 892: 2, 893: 2, 894: 1, 961: 8, 967: 8, 969: 8, 977: 8, 979: 8, 985: 8, 1001: 8, 1005: 6, 1009: 8, 1011: 8, 1013: 3, 1017: 8, 1020: 8, 1024: 8, 1025: 8, 1026: 8, 1027: 8, 1028: 8, 1029: 8, 1030: 8, 1031: 8, 1032: 2, 1033: 7, 1034: 7, 1105: 6, 1217: 8, 1221: 5, 1223: 8, 1225: 7, 1233: 8, 1249: 8, 1257: 6, 1259: 8, 1261: 8, 1263: 8, 1265: 8, 1267: 8, 1271: 8, 1280: 4, 1296: 4, 1300: 8, 1322: 6, 1328: 4, 1417: 8, 1601: 8, 1602: 8, 1603: 7, 1611: 8, 1618: 8, 1906: 8, 1907: 7, 1912: 7, 1914: 7, 1916: 7, 1919: 7, 1930: 7, 2016: 8, 2018: 8, 2019: 8, 2024: 8, 2026: 8
  }],
  CAR.CADILLAC_ATS: [{
    190: 6, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 2, 241: 6, 249: 8, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 368: 3, 381: 6, 384: 4, 386: 8, 388: 8, 393: 7, 398: 8, 401: 8, 407: 7, 413: 8, 417: 7, 419: 1, 422: 4, 426: 7, 431: 8, 442: 8, 451: 8, 452: 8, 453: 6, 455: 7, 456: 8, 462: 4, 479: 3, 481: 7, 485: 8, 487: 8, 489: 8, 491: 2, 493: 8, 497: 8, 499: 3, 500: 6, 501: 8, 508: 8, 510: 8, 528: 5, 532: 6, 534: 2, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 567: 5, 573: 1, 577: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 6, 707: 8, 715: 8, 717: 5, 719: 5, 723: 2, 753: 5, 761: 7, 801: 8, 804: 3, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 869: 4, 880: 6, 882: 8, 890: 1, 892: 2, 893: 2, 894: 1, 961: 8, 967: 4, 969: 8, 977: 8, 979: 8, 985: 5, 1001: 8, 1005: 6, 1009: 8, 1011: 6, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1033: 7, 1034: 7, 1105: 6, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1233: 8, 1241: 3, 1249: 8, 1257: 6, 1259: 8, 1261: 7, 1263: 4, 1265: 8, 1267: 1, 1271: 8, 1280: 4, 1296: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1417: 8, 1601: 8, 1904: 7, 1906: 7, 1907: 7, 1912: 7, 1916: 7, 1917: 7, 1918: 7, 1919: 7, 1920: 7, 1930: 7, 2016: 8, 2024: 8
  }],
  CAR.CHEVROLET_MALIBU: [{
    190: 6, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 2, 241: 6, 249: 8, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 328: 1, 352: 5, 381: 6, 384: 4, 386: 8, 388: 8, 393: 7, 398: 8, 407: 7, 413: 8, 417: 7, 419: 1, 422: 4, 426: 7, 431: 8, 442: 8, 451: 8, 452: 8, 453: 6, 455: 7, 456: 8, 479: 3, 481: 7, 485: 8, 487: 8, 489: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 508: 8, 510: 8, 528: 5, 532: 6, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 567: 5, 573: 1, 577: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 6, 707: 8, 715: 8, 717: 5, 753: 5, 761: 7, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 869: 4, 880: 6, 961: 8, 969: 8, 977: 8, 979: 8, 985: 5, 1001: 8, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1033: 7, 1034: 7, 1105: 6, 1217: 8, 1221: 5, 1223: 2, 1225: 7, 1233: 8, 1249: 8, 1257: 6, 1265: 8, 1267: 1, 1280: 4, 1296: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1417: 8, 1601: 8, 1906: 7, 1907: 7, 1912: 7, 1919: 7, 1930: 7, 2016: 8, 2024: 8
  }],
  CAR.GMC_ACADIA: [{
    190: 6, 192: 5, 193: 8, 197: 8, 199: 4, 201: 6, 208: 8, 209: 7, 211: 2, 241: 6, 249: 8, 288: 5, 289: 1, 290: 1, 298: 8, 304: 8, 309: 8, 313: 8, 320: 8, 322: 7, 328: 1, 352: 7, 368: 8, 381: 8, 384: 8, 386: 8, 388: 8, 393: 8, 398: 8, 413: 8, 417: 7, 419: 1, 422: 4, 426: 7, 431: 8, 442: 8, 451: 8, 452: 8, 453: 6, 454: 8, 455: 7, 458: 8, 460: 4, 462: 4, 463: 3, 479: 3, 481: 7, 485: 8, 489: 5, 497: 8, 499: 3, 500: 6, 501: 8, 508: 8, 510: 8, 512: 3, 530: 8, 532: 6, 534: 2, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 567: 5, 568: 2, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 6, 707: 8, 715: 8, 717: 5, 753: 5, 761: 7, 789: 5, 800: 6, 801: 8, 803: 8, 804: 3, 805: 8, 832: 8, 840: 5, 842: 5, 844: 8, 866: 4, 869: 4, 880: 6, 961: 8, 969: 8, 977: 8, 979: 8, 985: 5, 1001: 8, 1003: 5, 1005: 6, 1009: 8, 1017: 8, 1020: 8, 1033: 7, 1034: 7, 1105: 6, 1217: 8, 1221: 5, 1225: 8, 1233: 8, 1249: 8, 1257: 6, 1265: 8, 1267: 1, 1280: 4, 1296: 4, 1300: 8, 1322: 6, 1328: 4, 1417: 8, 1906: 7, 1907: 7, 1912: 7, 1914: 7, 1918: 7, 1919: 7, 1920: 7, 1930: 7
  },
  {
    190: 6, 193: 8, 197: 8, 199: 4, 201: 8, 208: 8, 209: 7, 211: 2, 241: 6, 249: 8, 288: 5, 289: 8, 298: 8, 304: 1, 309: 8, 313: 8, 320: 3, 322: 7, 328: 1, 338: 6, 340: 6, 352: 5, 381: 8, 384: 4, 386: 8, 388: 8, 393: 8, 398: 8, 413: 8, 417: 7, 419: 1, 422: 4, 426: 7, 431: 8, 442: 8, 451: 8, 452: 8, 453: 6, 454: 8, 455: 7, 462: 4, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 497: 8, 499: 3, 500: 6, 501: 8, 508: 8, 510: 8, 532: 6, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 567: 5, 573: 1, 577: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 6, 707: 8, 715: 8, 717: 5, 753: 5, 761: 7, 840: 5, 842: 5, 844: 8, 866: 4, 869: 4, 880: 6, 961: 8, 969: 8, 977: 8, 979: 8, 985: 5, 1001: 8, 1005: 6, 1009: 8, 1017: 8, 1020: 8, 1033: 7, 1034: 7, 1105: 6, 1217: 8, 1221: 5, 1225: 8, 1233: 8, 1249: 8, 1257: 6, 1265: 8, 1267: 1, 1280: 4, 1296: 4, 1300: 8, 1322: 6, 1328: 4, 1417: 8, 1601: 8, 1906: 7, 1907: 7, 1912: 7, 1914: 7, 1919: 7, 1920: 7, 1930: 7, 2016: 8, 2024: 8
  }],
  CAR.CADILLAC_ESCALADE: [{
    170: 8, 190: 6, 193: 8, 197: 8, 199: 4, 201: 8, 208: 8, 209: 7, 211: 2, 241: 6, 249: 8, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 381: 6, 384: 4, 386: 8, 388: 8, 393: 7, 398: 8, 407: 4, 413: 8, 417: 7, 419: 1, 422: 4, 426: 7, 431: 8, 442: 8, 451: 8, 452: 8, 453: 6, 454: 8, 455: 7, 460: 5, 462: 4, 463: 3, 479: 3, 481: 7, 485: 8, 487: 8, 489: 8, 497: 8, 499: 3, 500: 6, 501: 8, 508: 8, 510: 8, 532: 6, 534: 2, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 6, 707: 8, 715: 8, 717: 5, 719: 5, 761: 7, 801: 8, 804: 3, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 869: 4, 880: 6, 961: 8, 967: 4, 969: 8, 977: 8, 979: 8, 985: 5, 1001: 8, 1005: 6, 1009: 8, 1017: 8, 1019: 2, 1020: 8, 1033: 7, 1034: 7, 1105: 6, 1217: 8, 1221: 5, 1223: 2, 1225: 7, 1233: 8, 1249: 8, 1257: 6, 1265: 8, 1267: 1, 1280: 4, 1296: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1417: 8, 1609: 8, 1613: 8, 1649: 8, 1792: 8, 1798: 8, 1824: 8, 1825: 8, 1840: 8, 1842: 8, 1858: 8, 1860: 8, 1863: 8, 1872: 8, 1875: 8, 1882: 8, 1888: 8, 1889: 8, 1892: 8, 1906: 7, 1907: 7, 1912: 7, 1914: 7, 1917: 7, 1918: 7, 1919: 7, 1920: 7, 1930: 7, 1937: 8, 1953: 8, 1968: 8, 2001: 8, 2017: 8, 2018: 8, 2020: 8, 2026: 8
  }],
  CAR.CADILLAC_ESCALADE_ESV: [{
    309: 1, 848: 8, 849: 8, 850: 8, 851: 8, 852: 8, 853: 8, 854: 3, 1056: 6, 1057: 8, 1058: 8, 1059: 8, 1060: 8, 1061: 8, 1062: 8, 1063: 8, 1064: 8, 1065: 8, 1066: 8, 1067: 8, 1068: 8, 1120: 8, 1121: 8, 1122: 8, 1123: 8, 1124: 8, 1125: 8, 1126: 8, 1127: 8, 1128: 8, 1129: 8, 1130: 8, 1131: 8, 1132: 8, 1133: 8, 1134: 8, 1135: 8, 1136: 8, 1137: 8, 1138: 8, 1139: 8, 1140: 8, 1141: 8, 1142: 8, 1143: 8, 1146: 8, 1147: 8, 1148: 8, 1149: 8, 1150: 8, 1151: 8, 1216: 8, 1217: 8, 1218: 8, 1219: 8, 1220: 8, 1221: 8, 1222: 8, 1223: 8, 1224: 8, 1225: 8, 1226: 8, 1232: 8, 1233: 8, 1234: 8, 1235: 8, 1236: 8, 1237: 8, 1238: 8, 1239: 8, 1240: 8, 1241: 8, 1242: 8, 1787: 8, 1788: 8
  }],
  CAR.CADILLAC_ESCALADE_ESV_2019: [{
    715: 8, 840: 5, 717: 5, 869: 4, 880: 6, 289: 8, 454: 8, 842: 5, 460: 5, 463: 3, 801: 8, 170: 8, 190: 6, 241: 6, 201: 8, 417: 7, 211: 2, 419: 1, 398: 8, 426: 7, 487: 8, 442: 8, 451: 8, 452: 8, 453: 6, 479: 3, 311: 8, 500: 6, 647: 6, 193: 8, 707: 8, 197: 8, 209: 7, 199: 4, 455: 7, 313: 8, 481: 7, 485: 8, 489: 8, 249: 8, 393: 7, 407: 7, 413: 8, 422: 4, 431: 8, 501: 8, 499: 3, 810: 8, 508: 8, 381: 8, 462: 4, 532: 6, 562: 8, 386: 8, 761: 7, 573: 1, 554: 3, 719: 5, 560: 8, 1279: 4, 388: 8, 288: 5, 1005: 6, 497: 8, 844: 8, 961: 8, 967: 4, 977: 8, 979: 8, 985: 5, 1001: 8, 1017: 8, 1019: 2, 1020: 8, 1217: 8, 510: 8, 866: 4, 304: 1, 969: 8, 384: 4, 1033: 7, 1009: 8, 1034: 7, 1296: 4, 1930: 7, 1105: 5, 1013: 5, 1225: 7, 1919: 7, 320: 3, 534: 2, 352: 5, 298: 8, 1223: 2, 1233: 8, 608: 8, 1265: 8, 609: 6, 1267: 1, 1417: 8, 610: 6, 1906: 7, 611: 6, 612: 8, 613: 8, 208: 8, 564: 5, 309: 8, 1221: 5, 1280: 4, 1249: 8, 1907: 7, 1257: 6, 1300: 8, 1920: 7, 563: 5, 1322: 6, 1323: 4, 1328: 4, 1917: 7, 328: 1, 1912: 7, 1914: 7, 804: 3, 1918: 7
  }],
  CAR.CHEVROLET_BOLT_EUV: [{
    189: 7, 190: 7, 193: 8, 197: 8, 201: 8, 209: 7, 211: 3, 241: 6, 257: 8, 288: 5, 289: 8, 298: 8, 304: 3, 309: 8, 311: 8, 313: 8, 320: 4, 322: 7, 328: 1, 352: 5, 381: 8, 384: 4, 386: 8, 388: 8, 451: 8, 452: 8, 453: 6, 458: 5, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 497: 8, 500: 6, 501: 8, 528: 5, 532: 6, 560: 8, 562: 8, 563: 5, 565: 5, 566: 8, 587: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 707: 8, 715: 8, 717: 5, 753: 5, 761: 7, 789: 5, 800: 6, 810: 8, 840: 5, 842: 5, 844: 8, 848: 4, 869: 4, 880: 6, 977: 8, 1001: 8, 1017: 8, 1020: 8, 1217: 8, 1221: 5, 1233: 8, 1249: 8, 1265: 8, 1280: 4, 1296: 4, 1300: 8, 1611: 8, 1930: 7
  }],
  CAR.CHEVROLET_SILVERADO: [{
    190: 6, 193: 8, 197: 8, 201: 8, 208: 8, 209: 7, 211: 2, 241: 6, 249: 8, 257: 8, 288: 5, 289: 8, 298: 8, 304: 3, 309: 8, 311: 8, 313: 8, 320: 4, 322: 7, 328: 1, 352: 5, 381: 8, 384: 4, 386: 8, 388: 8, 413: 8, 451: 8, 452: 8, 453: 6, 455: 7, 460: 5, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 497: 8, 500: 6, 501: 8, 528: 5, 532: 6, 534: 2, 560: 8, 562: 8, 563: 5, 565: 5, 587: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 707: 8, 715: 8, 717: 5, 761: 7, 789: 5, 800: 6, 801: 8, 810: 8, 840: 5, 842: 5, 844: 8, 848: 4, 869: 4, 880: 6, 977: 8, 1001: 8, 1011: 6, 1017: 8, 1020: 8, 1033: 7, 1034: 7, 1217: 8, 1221: 5, 1233: 8, 1249: 8, 1259: 8, 1261: 7, 1263: 4, 1265: 8, 1267: 1, 1271: 8, 1280: 4, 1296: 4, 1300: 8, 1611: 8, 1930: 7
  }],
  CAR.CHEVROLET_EQUINOX: [{
    190: 6, 193: 8, 197: 8, 201: 8, 209: 7, 211: 2, 241: 6, 249: 8, 257: 8, 288: 5, 289: 8, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 328: 1, 352: 5, 381: 8, 384: 4, 386: 8, 388: 8, 413: 8, 451: 8, 452: 8, 453: 6, 455: 7, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 497: 8, 500: 6, 501: 8, 510: 8, 528: 5, 532: 6, 560: 8, 562: 8, 563: 5, 565: 5, 587: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 707: 8, 715: 8, 717: 5, 753: 5, 761: 7, 789: 5, 800: 6, 810: 8, 840: 5, 842: 5, 844: 8, 869: 4, 880: 6, 977: 8, 1001: 8, 1011: 6, 1017: 8, 1020: 8, 1033: 7, 1034: 7, 1217: 8, 1221: 5, 1233: 8, 1249: 8, 1259: 8, 1261: 7, 1263: 4, 1265: 8, 1267: 1, 1271: 8, 1280: 4, 1296: 4, 1300: 8, 1611: 8, 1930: 7
  },
  {
    190: 6, 201: 8, 211: 2, 717: 5, 241: 6, 451: 8, 298: 8, 452: 8, 453: 6, 479: 3, 485: 8, 249: 8, 500: 6, 587: 8, 1611: 8, 289: 8, 481: 7, 193: 8, 197: 8, 209: 7, 455: 7, 489: 8, 309: 8, 413: 8, 501: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 311: 8, 510: 8, 528: 5, 532: 6, 715: 8, 560: 8, 562: 8, 707: 8, 789: 5, 869: 4, 880: 6, 761: 7, 840: 5, 842: 5, 844: 8, 313: 8, 381: 8, 386: 8, 810: 8, 322: 7, 384: 4, 800: 6, 1033: 7, 1034: 7, 1296: 4, 753: 5, 388: 8, 288: 5, 497: 8, 463: 3, 304: 3, 977: 8, 1001: 8, 1280: 4, 320: 4, 352: 5, 563: 5, 565: 5, 1221: 5, 1011: 6, 1017: 8, 1020: 8, 1249: 8, 1300: 8, 328: 1, 1217: 8, 1233: 8, 1259: 8, 1261: 7, 1263: 4, 1265: 8, 1267: 1, 1930: 7, 1271: 8
  }],
}

FW_VERSIONS: dict[str, dict[tuple, list[bytes]]] = {
}
