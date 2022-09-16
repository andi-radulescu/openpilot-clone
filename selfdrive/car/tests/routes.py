#!/usr/bin/env python3
from collections import namedtuple

from selfdrive.car.chrysler.values import CAR as CHRYSLER
from selfdrive.car.gm.values import CAR as GM
from selfdrive.car.ford.values import CAR as FORD
from selfdrive.car.honda.values import CAR as HONDA
from selfdrive.car.hyundai.values import CAR as HYUNDAI
from selfdrive.car.nissan.values import CAR as NISSAN
from selfdrive.car.mazda.values import CAR as MAZDA
from selfdrive.car.subaru.values import CAR as SUBARU
from selfdrive.car.toyota.values import CAR as TOYOTA
from selfdrive.car.volkswagen.values import CAR as VOLKSWAGEN
from selfdrive.car.tesla.values import CAR as TESLA
from selfdrive.car.body.values import CAR as COMMA

# TODO: add routes for these cars
non_tested_cars = [
  FORD.ESCAPE_MK4,
  FORD.FOCUS_MK4,
  GM.CADILLAC_ATS,
  GM.HOLDEN_ASTRA,
  GM.MALIBU,
  GM.EQUINOX,
  GM.BOLT_EV,
  HYUNDAI.ELANTRA_GT_I30,
  HYUNDAI.GENESIS_G90,
  HYUNDAI.KIA_OPTIMA_H,
]

CarTestRoute = namedtuple('CarTestRoute', ['route', 'car_model', 'segment'], defaults=(None,))

routes = [
  CarTestRoute("efdf9af95e71cd84|2022-05-13--19-03-31", COMMA.BODY),

  CarTestRoute("0c94aa1e1296d7c6|2021-05-05--19-48-37", CHRYSLER.JEEP_CHEROKEE),
  CarTestRoute("91dfedae61d7bd75|2021-05-22--20-07-52", CHRYSLER.JEEP_CHEROKEE_2019),
  CarTestRoute("420a8e183f1aed48|2020-03-05--07-15-29", CHRYSLER.PACIFICA_2017_HYBRID),
  CarTestRoute("43a685a66291579b|2021-05-27--19-47-29", CHRYSLER.PACIFICA_2018),
  CarTestRoute("378472f830ee7395|2021-05-28--07-38-43", CHRYSLER.PACIFICA_2018_HYBRID),
  CarTestRoute("8190c7275a24557b|2020-01-29--08-33-58", CHRYSLER.PACIFICA_2019_HYBRID),
  CarTestRoute("3d84727705fecd04|2021-05-25--08-38-56", CHRYSLER.PACIFICA_2020),
  CarTestRoute("221c253375af4ee9|2022-06-15--18-38-24", CHRYSLER.RAM_1500),
  CarTestRoute("8fb5eabf914632ae|2022-08-04--17-28-53", CHRYSLER.RAM_HD, segment=6),

  CarTestRoute("62241b0c7fea4589|2022-09-01--15-32-49", FORD.EXPLORER_MK6),
  #TestRoute("f1b4c567731f4a1b|2018-04-30--10-15-35", FORD.FUSION),

  CarTestRoute("7cc2a8365b4dd8a9|2018-12-02--12-10-44", GM.ACADIA),
  CarTestRoute("aa20e335f61ba898|2019-02-05--16-59-04", GM.BUICK_REGAL),
  CarTestRoute("46460f0da08e621e|2021-10-26--07-21-46", GM.ESCALADE_ESV),
  CarTestRoute("c950e28c26b5b168|2018-05-30--22-03-41", GM.VOLT),
  CarTestRoute("f08912a233c1584f|2022-08-11--18-02-41", GM.BOLT_EUV, segment=1),
  CarTestRoute("38aa7da107d5d252|2022-08-15--16-01-12", GM.SILVERADO),

  CarTestRoute("0e7a2ba168465df5|2020-10-18--14-14-22", HONDA.ACURA_RDX_3G),
  CarTestRoute("a74b011b32b51b56|2020-07-26--17-09-36", HONDA.CIVIC),
  CarTestRoute("a859a044a447c2b0|2020-03-03--18-42-45", HONDA.CRV_EU),
  CarTestRoute("68aac44ad69f838e|2021-05-18--20-40-52", HONDA.CRV),
  CarTestRoute("14fed2e5fa0aa1a5|2021-05-25--14-59-42", HONDA.CRV_HYBRID),
  CarTestRoute("52f3e9ae60c0d886|2021-05-23--15-59-43", HONDA.FIT),
  CarTestRoute("2c4292a5cd10536c|2021-08-19--21-32-15", HONDA.FREED),
  CarTestRoute("03be5f2fd5c508d1|2020-04-19--18-44-15", HONDA.HRV),
  CarTestRoute("917b074700869333|2021-05-24--20-40-20", HONDA.ACURA_ILX),
  CarTestRoute("81722949a62ea724|2019-04-06--15-19-25", HONDA.ODYSSEY_CHN),
  CarTestRoute("08a3deb07573f157|2020-03-06--16-11-19", HONDA.ACCORD),  # 1.5T
  CarTestRoute("1da5847ac2488106|2021-05-24--19-31-50", HONDA.ACCORD),  # 2.0T
  CarTestRoute("085ac1d942c35910|2021-03-25--20-11-15", HONDA.ACCORD),  # 2021 with new style HUD msgs
  CarTestRoute("07585b0da3c88459|2021-05-26--18-52-04", HONDA.ACCORDH),
  CarTestRoute("f29e2b57a55e7ad5|2021-03-24--20-52-38", HONDA.ACCORDH), # 2021 with new style HUD msgs
  CarTestRoute("1ad763dd22ef1a0e|2020-02-29--18-37-03", HONDA.CRV_5G),
  CarTestRoute("0a96f86fcfe35964|2020-02-05--07-25-51", HONDA.ODYSSEY),
  CarTestRoute("d83f36766f8012a5|2020-02-05--18-42-21", HONDA.CIVIC_BOSCH_DIESEL),
  CarTestRoute("f0890d16a07a236b|2021-05-25--17-27-22", HONDA.INSIGHT),
  CarTestRoute("07d37d27996096b6|2020-03-04--21-57-27", HONDA.PILOT),
  CarTestRoute("684e8f96bd491a0e|2021-11-03--11-08-42", HONDA.PASSPORT),
  CarTestRoute("0a78dfbacc8504ef|2020-03-04--13-29-55", HONDA.CIVIC_BOSCH),
  CarTestRoute("f34a60d68d83b1e5|2020-10-06--14-35-55", HONDA.ACURA_RDX),
  CarTestRoute("54fd8451b3974762|2021-04-01--14-50-10", HONDA.RIDGELINE),
  CarTestRoute("2d5808fae0b38ac6|2021-09-01--17-14-11", HONDA.HONDA_E),
  CarTestRoute("f44aa96ace22f34a|2021-12-22--06-22-31", HONDA.CIVIC_2022),

  CarTestRoute("6fe86b4e410e4c37|2020-07-22--16-27-13", HYUNDAI.HYUNDAI_GENESIS),
  CarTestRoute("70c5bec28ec8e345|2020-08-08--12-22-23", HYUNDAI.GENESIS_G70),
  CarTestRoute("6b301bf83f10aa90|2020-11-22--16-45-07", HYUNDAI.GENESIS_G80),
  CarTestRoute("4dbd55df87507948|2022-03-01--09-45-38", HYUNDAI.SANTA_FE),
  CarTestRoute("bf43d9df2b660eb0|2021-09-23--14-16-37", HYUNDAI.SANTA_FE_2022),
  CarTestRoute("37398f32561a23ad|2021-11-18--00-11-35", HYUNDAI.SANTA_FE_HEV_2022),
  CarTestRoute("656ac0d830792fcc|2021-12-28--14-45-56", HYUNDAI.SANTA_FE_PHEV_2022, segment=1),
  CarTestRoute("e0e98335f3ebc58f|2021-03-07--16-38-29", HYUNDAI.KIA_CEED),
  CarTestRoute("7653b2bce7bcfdaa|2020-03-04--15-34-32", HYUNDAI.KIA_OPTIMA),
  CarTestRoute("c75a59efa0ecd502|2021-03-11--20-52-55", HYUNDAI.KIA_SELTOS),
  CarTestRoute("5b7c365c50084530|2020-04-15--16-13-24", HYUNDAI.SONATA),
  CarTestRoute("b2a38c712dcf90bd|2020-05-18--18-12-48", HYUNDAI.SONATA_LF),
  CarTestRoute("fb3fd42f0baaa2f8|2022-03-30--15-25-05", HYUNDAI.TUCSON),
  CarTestRoute("36e10531feea61a4|2022-07-25--13-37-42", HYUNDAI.TUCSON_HYBRID_4TH_GEN),
  CarTestRoute("5875672fc1d4bf57|2020-07-23--21-33-28", HYUNDAI.KIA_SORENTO),
  CarTestRoute("9c917ba0d42ffe78|2020-04-17--12-43-19", HYUNDAI.PALISADE),
  CarTestRoute("22de8111a8c5463c|2022-07-29--13-34-49", HYUNDAI.IONIQ_5),
  CarTestRoute("3f29334d6134fcd4|2022-03-30--22-00-50", HYUNDAI.IONIQ_PHEV_2019),
  CarTestRoute("fa8db5869167f821|2021-06-10--22-50-10", HYUNDAI.IONIQ_PHEV),
  CarTestRoute("2c5cf2dd6102e5da|2020-12-17--16-06-44", HYUNDAI.IONIQ_EV_2020),
  CarTestRoute("610ebb9faaad6b43|2020-06-13--15-28-36", HYUNDAI.IONIQ_EV_LTD),
  CarTestRoute("2c5cf2dd6102e5da|2020-06-26--16-00-08", HYUNDAI.IONIQ),
  CarTestRoute("ab59fe909f626921|2021-10-18--18-34-28", HYUNDAI.IONIQ_HEV_2022),
  CarTestRoute("22d955b2cd499c22|2020-08-10--19-58-21", HYUNDAI.KONA),
  CarTestRoute("efc48acf44b1e64d|2021-05-28--21-05-04", HYUNDAI.KONA_EV),
  CarTestRoute("ff973b941a69366f|2022-07-28--22-01-19", HYUNDAI.KONA_EV_2022, segment=11),
  CarTestRoute("49f3c13141b6bc87|2021-07-28--08-05-13", HYUNDAI.KONA_HEV),
  CarTestRoute("5dddcbca6eb66c62|2020-07-26--13-24-19", HYUNDAI.KIA_STINGER),
  CarTestRoute("d624b3d19adce635|2020-08-01--14-59-12", HYUNDAI.VELOSTER),
  CarTestRoute("d824e27e8c60172c|2022-05-19--16-15-28", HYUNDAI.KIA_EV6),
  CarTestRoute("007d5e4ad9f86d13|2021-09-30--15-09-23", HYUNDAI.KIA_K5_2021),
  CarTestRoute("50c6c9b85fd1ff03|2020-10-26--17-56-06", HYUNDAI.KIA_NIRO_EV),
  CarTestRoute("173219cf50acdd7b|2021-07-05--10-27-41", HYUNDAI.KIA_NIRO_PHEV),
  CarTestRoute("34a875f29f69841a|2021-07-29--13-02-09", HYUNDAI.KIA_NIRO_HEV_2021),
  CarTestRoute("50a2212c41f65c7b|2021-05-24--16-22-06", HYUNDAI.KIA_FORTE),
  CarTestRoute("c5ac319aa9583f83|2021-06-01--18-18-31", HYUNDAI.ELANTRA),
  CarTestRoute("82e9cdd3f43bf83e|2021-05-15--02-42-51", HYUNDAI.ELANTRA_2021),
  CarTestRoute("715ac05b594e9c59|2021-06-20--16-21-07", HYUNDAI.ELANTRA_HEV_2021),
  CarTestRoute("7120aa90bbc3add7|2021-08-02--07-12-31", HYUNDAI.SONATA_HYBRID),
  CarTestRoute("715ac05b594e9c59|2021-10-27--23-24-56", HYUNDAI.GENESIS_G70_2020),

  CarTestRoute("00c829b1b7613dea|2021-06-24--09-10-10", TOYOTA.ALPHARD_TSS2),
  CarTestRoute("912119ebd02c7a42|2022-03-19--07-24-50", TOYOTA.ALPHARDH_TSS2),
  CarTestRoute("000cf3730200c71c|2021-05-24--10-42-05", TOYOTA.AVALON),
  CarTestRoute("0bb588106852abb7|2021-05-26--12-22-01", TOYOTA.AVALON_2019),
  CarTestRoute("87bef2930af86592|2021-05-30--09-40-54", TOYOTA.AVALONH_2019),
  CarTestRoute("e9966711cfb04ce3|2022-01-11--07-59-43", TOYOTA.AVALON_TSS2),
  CarTestRoute("eca1080a91720a54|2022-03-17--13-32-29", TOYOTA.AVALONH_TSS2),
  CarTestRoute("6cdecc4728d4af37|2020-02-23--15-44-18", TOYOTA.CAMRY),
  CarTestRoute("3456ad0cd7281b24|2020-12-13--17-45-56", TOYOTA.CAMRY_TSS2),
  CarTestRoute("ffccc77938ddbc44|2021-01-04--16-55-41", TOYOTA.CAMRYH_TSS2),
  CarTestRoute("54034823d30962f5|2021-05-24--06-37-34", TOYOTA.CAMRYH),
  CarTestRoute("4e45c89c38e8ec4d|2021-05-02--02-49-28", TOYOTA.COROLLA),
  CarTestRoute("5f5afb36036506e4|2019-05-14--02-09-54", TOYOTA.COROLLA_TSS2),
  CarTestRoute("5ceff72287a5c86c|2019-10-19--10-59-02", TOYOTA.COROLLAH_TSS2),
  CarTestRoute("d2525c22173da58b|2021-04-25--16-47-04", TOYOTA.PRIUS),
  CarTestRoute("b14c5b4742e6fc85|2020-07-28--19-50-11", TOYOTA.RAV4),
  CarTestRoute("32a7df20486b0f70|2020-02-06--16-06-50", TOYOTA.RAV4H),
  CarTestRoute("cdf2f7de565d40ae|2019-04-25--03-53-41", TOYOTA.RAV4_TSS2),
  CarTestRoute("a5c341bb250ca2f0|2022-05-18--16-05-17", TOYOTA.RAV4_TSS2_2022),
  CarTestRoute("7e34a988419b5307|2019-12-18--19-13-30", TOYOTA.RAV4H_TSS2),
  CarTestRoute("2475fb3eb2ffcc2e|2022-04-29--12-46-23", TOYOTA.RAV4H_TSS2_2022),
  CarTestRoute("e6a24be49a6cd46e|2019-10-29--10-52-42", TOYOTA.LEXUS_ES_TSS2),
  CarTestRoute("da23c367491f53e2|2021-05-21--09-09-11", TOYOTA.LEXUS_CTH, segment=3),
  CarTestRoute("f49e8041283f2939|2019-05-30--11-51-51", TOYOTA.LEXUS_ESH_TSS2),
  CarTestRoute("37041c500fd30100|2020-12-30--12-17-24", TOYOTA.LEXUS_ESH),
  CarTestRoute("32696cea52831b02|2021-11-19--18-13-30", TOYOTA.LEXUS_RC),
  CarTestRoute("886fcd8408d570e9|2020-01-29--02-18-55", TOYOTA.LEXUS_RX),
  CarTestRoute("d27ad752e9b08d4f|2021-05-26--19-39-51", TOYOTA.LEXUS_RXH),
  CarTestRoute("01b22eb2ed121565|2020-02-02--11-25-51", TOYOTA.LEXUS_RX_TSS2),
  CarTestRoute("b74758c690a49668|2020-05-20--15-58-57", TOYOTA.LEXUS_RXH_TSS2),
  CarTestRoute("ec429c0f37564e3c|2020-02-01--17-28-12", TOYOTA.LEXUS_NXH),
  CarTestRoute("964c09eb11ca8089|2020-11-03--22-04-00", TOYOTA.LEXUS_NX),
  CarTestRoute("3fd5305f8b6ca765|2021-04-28--19-26-49", TOYOTA.LEXUS_NX_TSS2),
  CarTestRoute("09ae96064ed85a14|2022-06-09--12-22-31", TOYOTA.LEXUS_NXH_TSS2),
  CarTestRoute("0a302ffddbb3e3d3|2020-02-08--16-19-08", TOYOTA.HIGHLANDER_TSS2),
  CarTestRoute("437e4d2402abf524|2021-05-25--07-58-50", TOYOTA.HIGHLANDERH_TSS2),
  CarTestRoute("3183cd9b021e89ce|2021-05-25--10-34-44", TOYOTA.HIGHLANDER),
  CarTestRoute("80d16a262e33d57f|2021-05-23--20-01-43", TOYOTA.HIGHLANDERH),
  CarTestRoute("eb6acd681135480d|2019-06-20--20-00-00", TOYOTA.SIENNA),
  CarTestRoute("2e07163a1ba9a780|2019-08-25--13-15-13", TOYOTA.LEXUS_IS),
  CarTestRoute("0a0de17a1e6a2d15|2020-09-21--21-24-41", TOYOTA.PRIUS_TSS2),
  CarTestRoute("9b36accae406390e|2021-03-30--10-41-38", TOYOTA.MIRAI),
  CarTestRoute("cd9cff4b0b26c435|2021-05-13--15-12-39", TOYOTA.CHR),
  CarTestRoute("57858ede0369a261|2021-05-18--20-34-20", TOYOTA.CHRH),
  CarTestRoute("14623aae37e549f3|2021-10-24--01-20-49", TOYOTA.PRIUS_V),

  CarTestRoute("202c40641158a6e5|2021-09-21--09-43-24", VOLKSWAGEN.ARTEON_MK1),
  CarTestRoute("2c68dda277d887ac|2021-05-11--15-22-20", VOLKSWAGEN.ATLAS_MK1),
  CarTestRoute("cae14e88932eb364|2021-03-26--14-43-28", VOLKSWAGEN.GOLF_MK7),
  CarTestRoute("58a7d3b707987d65|2021-03-25--17-26-37", VOLKSWAGEN.JETTA_MK7),
  CarTestRoute("4d134e099430fba2|2021-03-26--00-26-06", VOLKSWAGEN.PASSAT_MK8),
  CarTestRoute("3cfdec54aa035f3f|2022-07-19--23-45-10", VOLKSWAGEN.PASSAT_NMS),
  CarTestRoute("0cd0b7f7e31a3853|2021-11-03--19-30-22", VOLKSWAGEN.POLO_MK6),
  CarTestRoute("7d82b2f3a9115f1f|2021-10-21--15-39-42", VOLKSWAGEN.TAOS_MK1),
  CarTestRoute("2744c89a8dda9a51|2021-07-24--21-28-06", VOLKSWAGEN.TCROSS_MK1),
  CarTestRoute("2cef8a0b898f331a|2021-03-25--20-13-57", VOLKSWAGEN.TIGUAN_MK2),
  CarTestRoute("a589dcc642fdb10a|2021-06-14--20-54-26", VOLKSWAGEN.TOURAN_MK2),
  CarTestRoute("a459f4556782eba1|2021-09-19--09-48-00", VOLKSWAGEN.TRANSPORTER_T61),
  CarTestRoute("0cd0b7f7e31a3853|2021-11-18--00-38-32", VOLKSWAGEN.TROC_MK1),
  CarTestRoute("07667b885add75fd|2021-01-23--19-48-42", VOLKSWAGEN.AUDI_A3_MK3),
  CarTestRoute("6c6b466346192818|2021-06-06--14-17-47", VOLKSWAGEN.AUDI_Q2_MK1),
  CarTestRoute("0cd0b7f7e31a3853|2021-12-03--03-12-05", VOLKSWAGEN.AUDI_Q3_MK2),
  CarTestRoute("8f205bdd11bcbb65|2021-03-26--01-00-17", VOLKSWAGEN.SEAT_ATECA_MK1),
  CarTestRoute("fc6b6c9a3471c846|2021-05-27--13-39-56", VOLKSWAGEN.SEAT_LEON_MK3),
  CarTestRoute("12d6ae3057c04b0d|2021-09-15--00-04-07", VOLKSWAGEN.SKODA_KAMIQ_MK1),
  CarTestRoute("12d6ae3057c04b0d|2021-09-04--21-21-21", VOLKSWAGEN.SKODA_KAROQ_MK1),
  CarTestRoute("90434ff5d7c8d603|2021-03-15--12-07-31", VOLKSWAGEN.SKODA_KODIAQ_MK1),
  CarTestRoute("66e5edc3a16459c5|2021-05-25--19-00-29", VOLKSWAGEN.SKODA_OCTAVIA_MK3),
  CarTestRoute("026b6d18fba6417f|2021-03-26--09-17-04", VOLKSWAGEN.SKODA_SCALA_MK1),
  CarTestRoute("b2e9858e29db492b|2021-03-26--16-58-42", VOLKSWAGEN.SKODA_SUPERB_MK3),

  CarTestRoute("3c8f0c502e119c1c|2020-06-30--12-58-02", SUBARU.ASCENT),
  CarTestRoute("c321c6b697c5a5ff|2020-06-23--11-04-33", SUBARU.FORESTER),
  CarTestRoute("791340bc01ed993d|2019-03-10--16-28-08", SUBARU.IMPREZA),
  CarTestRoute("8bf7e79a3ce64055|2021-05-24--09-36-27", SUBARU.IMPREZA_2020),
  CarTestRoute("1bbe6bf2d62f58a8|2022-07-14--17-11-43", SUBARU.OUTBACK, segment=10),
  CarTestRoute("c56e69bbc74b8fad|2022-08-18--09-43-51", SUBARU.LEGACY, segment=3),
  # Pre-global, dashcam
  CarTestRoute("95441c38ae8c130e|2020-06-08--12-10-17", SUBARU.FORESTER_PREGLOBAL),
  CarTestRoute("df5ca7660000fba8|2020-06-16--17-37-19", SUBARU.LEGACY_PREGLOBAL),
  CarTestRoute("5ab784f361e19b78|2020-06-08--16-30-41", SUBARU.OUTBACK_PREGLOBAL),
  CarTestRoute("e19eb5d5353b1ac1|2020-08-09--14-37-56", SUBARU.OUTBACK_PREGLOBAL_2018),

  CarTestRoute("fbbfa6af821552b9|2020-03-03--08-09-43", NISSAN.XTRAIL),
  CarTestRoute("5b7c365c50084530|2020-03-25--22-10-13", NISSAN.LEAF),
  CarTestRoute("22c3dcce2dd627eb|2020-12-30--16-38-48", NISSAN.LEAF_IC),
  CarTestRoute("059ab9162e23198e|2020-05-30--09-41-01", NISSAN.ROGUE),
  CarTestRoute("b72d3ec617c0a90f|2020-12-11--15-38-17", NISSAN.ALTIMA),

  CarTestRoute("32a319f057902bb3|2020-04-27--15-18-58", MAZDA.CX5),
  CarTestRoute("10b5a4b380434151|2020-08-26--17-11-45", MAZDA.CX9),
  CarTestRoute("74f1038827005090|2020-08-26--20-05-50", MAZDA.MAZDA3),
  CarTestRoute("fb53c640f499b73d|2021-06-01--04-17-56", MAZDA.MAZDA6),
  CarTestRoute("f6d5b1a9d7a1c92e|2021-07-08--06-56-59", MAZDA.CX9_2021),
  CarTestRoute("a4af1602d8e668ac|2022-02-03--12-17-07", MAZDA.CX5_2022),

  CarTestRoute("6c14ee12b74823ce|2021-06-30--11-49-02", TESLA.AP1_MODELS),
  CarTestRoute("bb50caf5f0945ab1|2021-06-19--17-20-18", TESLA.AP2_MODELS),

  # Segments that test specific issues
  # Controls mismatch due to interceptor threshold
  CarTestRoute("cfb32f0fb91b173b|2022-04-06--14-54-45", HONDA.CIVIC, segment=21),
  CarTestRoute("5a8762b91fc70467|2022-04-14--21-26-20", TOYOTA.RAV4, segment=2),
  # Controls mismatch due to standstill threshold
  CarTestRoute("bec2dcfde6a64235|2022-04-08--14-21-32", HONDA.CRV_HYBRID, segment=22),
]
