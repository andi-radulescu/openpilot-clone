# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu


# Steer torque limits

class CarControllerParams:
  STEER_MAX = 600                 # max_steer 2048
  STEER_STEP = 1                  # how often we update the steer cmd
  STEER_DELTA_UP = 10             # torque increase per refresh
  STEER_DELTA_DOWN = 20           # torque decrease per refresh
  STEER_DRIVER_ALLOWANCE = 15     # allowed driver torque before start limiting
  STEER_DRIVER_MULTIPLIER = 1     # weight driver torque
  STEER_DRIVER_FACTOR = 1         # from dbc

class CAR:
  CX5 = "Mazda CX-5 2017"
  CX9 = "Mazda CX-9 2017"
  Mazda3 = "Mazda3 2017"

class LKAS_LIMITS:
  STEER_THRESHOLD = 15
  DISABLE_SPEED = 45    # kph
  ENABLE_SPEED = 52     # kph

class Buttons:
  NONE = 0
  SET_PLUS = 1
  SET_MINUS = 2
  RESUME = 3
  CANCEL = 4


FW_VERSIONS = {
  CAR.CX5: {
    (Ecu.eps, 0x730, None): [
      b'KJ01-3210X-G-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KJ01-3210X-M-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'PYNF-188K2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX38-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX2G-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K123-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'K123-437K2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KN0W-437K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KBJ5-437K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-T\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-V\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-N\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'PYNC-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX39-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYB2-21PS1-G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  },

  CAR.CX9 : {
    (Ecu.eps, 0x730, None): [
      b'KJ01-3210X-L-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'PX23-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PXN8-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K131-67XK2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'TN40-437K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'TA0B-437K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-V\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-K\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'PYD5-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PXM7-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  },

  CAR.Mazda3: {
    (Ecu.eps, 0x730, None): [
      b'K070-3210X-C-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KR11-3210X-K-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'P5JD-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYKC-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K131-67XK2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B63C-67XK2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'B45A-437AS-0-08\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-T\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'P52G-21PS1-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYKE-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  }
}


DBC = {
  CAR.CX5: dbc_dict('mazda_2017', None),
  CAR.CX9: dbc_dict('mazda_2017', None),
  CAR.Mazda3: dbc_dict('mazda_2017', None),
}

GEN1 = [ CAR.CX5, CAR.CX9, CAR.Mazda3 ]
