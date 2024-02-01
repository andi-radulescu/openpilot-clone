import math
import numpy as np
from collections import deque

from cereal import log
from openpilot.common.numpy_fast import interp
from openpilot.selfdrive.controls.lib.latcontrol import LatControl
from openpilot.selfdrive.controls.lib.pid import PIDController
from openpilot.selfdrive.controls.lib.vehicle_model import ACCELERATION_DUE_TO_GRAVITY
from openpilot.selfdrive.controls.lib.drive_helpers import get_friction

# At higher speeds (25+mph) we can assume:
# Lateral acceleration achieved by a specific car correlates to
# torque applied to the steering rack. It does not correlate to
# wheel slip, or to speed.

# This controller applies torque to achieve desired lateral
# accelerations. To compensate for the low speed effects we
# use a LOW_SPEED_FACTOR in the error. Additionally, there is
# friction in the steering wheel that needs to be overcome to
# move it at all, this is compensated for too.

LOW_SPEED_X = [0, 10, 20, 30]
LOW_SPEED_Y = [15, 13, 10, 5]


class NanoFFModel:
  def __init__(self, temperature=1.0):
    # self.w_1 = [[3.1900432109832764, -0.37573888897895813, -1.3121652603149414, 2.6689391136169434, 1.5531493425369263, 1.7823995351791382, 3.4191055297851562, 1.7675808668136597], [-0.7232083678245544, -0.06553429365158081, -0.05937732011079788, -0.6986712217330933, -0.18061856925487518, -0.4962347149848938, -0.8380135893821716, -0.3662603199481964], [-0.03277115896344185, 0.03201576694846153, -0.025812357664108276, 0.06850704550743103, 0.4274134039878845, -0.004680467303842306, -0.05513480678200722, 0.015983834862709045], [-0.30559229850769043, -0.27125728130340576, -0.39627915620803833, 0.06569751352071762, 0.26363715529441833, 0.06277585029602051, -0.38928478956222534, 0.10859646648168564], [1.2827545404434204, 1.7096779346466064, 0.7163336277008057, 0.8644662499427795, -0.39612334966659546, -0.03487994521856308, 1.605427622795105, -0.1349191665649414], [0.9179061055183411, 2.3207454681396484, 1.3605477809906006, 0.4095320403575897, -0.8882166743278503, -0.500495970249176, 1.1497553586959839, -0.5403992533683777], [0.35833898186683655, 2.8853394985198975, 1.9096674919128418, -0.06141189485788345, -1.646935224533081, -1.015617847442627, 0.5076309442520142, -1.0497525930404663], [-0.6210983991622925, -0.12343478947877884, -0.03978592902421951, -0.6785944104194641, -0.13170389831066132, -0.5560221672058105, -0.8075632452964783, -0.3575599193572998], [-0.5296007990837097, -0.389423668384552, -0.26156967878341675, -0.42312613129615784, 0.12104514241218567, -0.2939698100090027, -0.6980560421943665, -0.16298672556877136], [-0.2567983567714691, -0.5941768884658813, -0.5542563796043396, -0.2837754189968109, 0.4007265269756317, -0.1560964435338974, -0.36720964312553406, 0.04063839092850685], [0.012145349755883217, 0.18805164098739624, 0.0614439956843853, -0.07154802978038788, 0.5043861865997314, -0.049626994878053665, -0.05966878682374954, -0.10735032707452774], [0.01650974527001381, 0.001830110209994018, -0.04924454540014267, -0.05984148010611534, 0.5003781914710999, -0.04049041122198105, -0.06777270138263702, -0.016508804634213448], [-0.06617162376642227, 0.029375631362199783, -0.02804550901055336, 0.030467022210359573, 0.42632168531417847, -0.024852434173226357, -0.0030907196924090385, -0.16551297903060913], [-0.32580259442329407, -0.24488748610019684, -0.32683396339416504, -0.01919000968337059, 0.12490897625684738, 0.17895494401454926, -0.34487688541412354, 0.11210019886493683], [-0.2696765661239624, -0.3028377294540405, -0.24527736008167267, -0.08745969831943512, 0.2497100532054901, 0.07265375554561615, -0.37013161182403564, 0.17590118944644928], [-0.2743346691131592, -0.16069960594177246, -0.22537817060947418, -0.043523821979761124, 0.14299538731575012, 0.06332743912935257, -0.3213661313056946, 0.10957325249910355]]  # noqa: E501
    # self.b_1 = [-0.8718048334121704, -0.5246109366416931, -0.30594491958618164, -0.590533435344696, -0.3367057740688324, -0.3095954954624176, -0.8740265369415283, -0.3223787844181061]  # noqa: E501
    # self.w_2 = [[0.8718569874763489, 0.980969250202179, -1.0938196182250977, 0.5162032842636108], [-0.83515465259552, 0.02803085558116436, 1.0227752923965454, -0.3231082558631897], [-1.2006933689117432, -0.1881900131702423, 1.3541123867034912, -1.001417875289917], [0.5682749152183533, 0.27409738302230835, -0.8192962408065796, -0.03731514886021614], [0.5748910903930664, -0.007078315131366253, -0.3542194366455078, 0.5303947329521179], [0.6065377593040466, -0.4995797276496887, -0.8026412129402161, 0.3358980417251587], [1.2657983303070068, 1.0652618408203125, -1.3863341808319092, 0.6090320348739624], [0.5388105511665344, -0.06839455664157867, -0.7005999088287354, 0.5903877019882202]]  # noqa: E501
    # self.b_2 = [-0.5377247333526611, -0.05827830359339714, 0.6316986083984375, -0.016132982447743416]
    # self.w_3 = [[1.0667357444763184, 0.13138769567012787], [0.22754108905792236, -1.3573530912399292], [-1.8196125030517578, -2.071134567260742], [0.5297592878341675, -0.492388516664505]]  # noqa: E501
    # self.b_3 = [0.12318920344114304, -0.6744083762168884]
    # self.input_norm_mat = np.array([[-3.0, 3.0], [-3.0, 3.0], [0.0, 30.0], [-3.0, 3.0], [-3.0, 3.0], [-3.0, 3.0], [-3.0, 3.0], [-3.0, 3.0], [-3.0, 3.0], [-3.0, 3.0], [0.0, 30.0], [0.0, 30.0], [0.0, 30.0], [-3.0, 3.0], [-3.0, 3.0], [-3.0, 3.0]])  # noqa: E501
    # self.output_norm_mat = np.array([-1.0, 1.0])

    self.w_1 = [[1.9422959089279175, -0.9847834706306458, -0.9613131880760193, -2.198113203048706, 1.5321210622787476, 1.7586524486541748, 1.9867875576019287, 1.3703876733779907, -1.051804542541504, -0.5574182868003845, 1.6435242891311646, -1.3621861934661865, -0.028627924621105194, 2.1614179611206055, 2.0950560569763184, 1.9901591539382935], [-0.9745683670043945, 1.0905977487564087, 1.0745439529418945, 0.9586119055747986, -0.9638321995735168, -1.0295310020446777, -0.9495574235916138, -1.176953673362732, 0.8788508176803589, 1.1749635934829712, -1.2604857683181763, 0.7419278621673584, 1.2390682697296143, -0.9672487378120422, -1.2200286388397217, -0.9324063062667847], [-0.12387784570455551, -0.0407126359641552, -0.05074620619416237, -0.08777984976768494, -0.20455290377140045, -0.1739305853843689, 0.17806462943553925, -0.06580118834972382, -0.1088675782084465, -0.0043353973887860775, 0.0002649461675900966, -0.05668012797832489, 0.07978509366512299, 0.13196025788784027, -0.027961138635873795, -0.03901946172118187], [-0.22391490638256073, -0.024727702140808105, -0.21141496300697327, 0.1765599101781845, -0.06368886679410934, 0.022838708013296127, -0.20057620108127594, 0.26035305857658386, -0.318171888589859, -0.21744585037231445, -0.20366033911705017, -0.06565551459789276, -0.11233817785978317, -0.18531544506549835, -0.14991961419582367, 0.007961144670844078]]  # noqa: E501
    self.b_1 = [-0.35672950744628906, 0.18491682410240173, 0.22465860843658447, 0.6119869947433472, -0.2383432537317276, -0.33294323086738586, -0.5639381408691406, -0.3633899390697479, 0.3513927757740021, 0.19043372571468353, -0.23215575516223907, 0.4160981774330139, 0.023985689505934715, -0.6336583495140076, -0.4169510304927826, -0.5681884288787842]  # noqa: E501
    self.w_2 = [[-0.8392295837402344, -0.28107044100761414, 0.40190035104751587, -0.6540709733963013, 0.2356407791376114, 0.5670640468597412, 0.5706198811531067, 0.6413172483444214], [0.7801594734191895, 0.6748386025428772, -0.34215694665908813, 0.49990716576576233, -0.15191718935966492, -0.5652638077735901, -0.6177380084991455, -0.6130874752998352], [0.8095894455909729, 0.6083434820175171, -0.4116186797618866, 0.6137518882751465, -0.08394702523946762, -0.6791449785232544, -0.5387187004089355, -0.7261633276939392], [1.6426796913146973, -0.1565474420785904, -1.3245469331741333, 1.3871818780899048, -1.5498470067977905, -1.4927012920379639, -1.5558788776397705, -1.775301218032837], [-0.3760233521461487, -0.43539997935295105, 0.17037644982337952, -0.38370442390441895, -0.15139888226985931, 0.3016430139541626, 0.2942749559879303, 0.3210645914077759], [-0.6127520799636841, -0.4905199408531189, 0.3644622564315796, -0.5245510935783386, 0.005884596612304449, 0.48151859641075134, 0.4450797736644745, 0.5949309468269348], [-0.9166551232337952, -0.028048966079950333, 0.6739140748977661, -0.6761773824691772, 0.7226991653442383, 0.6890302300453186, 0.8184887766838074, 0.8127145767211914], [-0.5186765193939209, -0.880578875541687, 0.3138599395751953, -0.44278866052627563, -0.2448251098394394, 0.448860764503479, 0.40350595116615295, 0.4343448877334595], [0.8294195532798767, 0.3180135488510132, -0.5223674178123474, 0.6903705596923828, -0.4641018211841583, -0.7336373329162598, -0.6318897008895874, -0.7226791381835938], [0.4860416352748871, 0.8090940713882446, -0.2903136909008026, 0.4284409284591675, 0.24223358929157257, -0.43025994300842285, -0.4037773311138153, -0.41546788811683655], [-0.6543788909912109, -0.8889179229736328, 0.3653898239135742, -0.5605858564376831, 0.044624291360378265, 0.6545067429542542, 0.5166909098625183, 0.5671386122703552], [0.8660609722137451, 0.03590446710586548, -0.5207877159118652, 0.7524996995925903, -0.7398838996887207, -0.6782453656196594, -0.7077322602272034, -0.829913318157196], [0.3095931112766266, 0.84073805809021, -0.16923116147518158, 0.28761976957321167, 0.5492982864379883, -0.09209482371807098, -0.26433995366096497, -0.24155624210834503], [-1.057140588760376, 0.05023855343461037, 0.7248144745826721, -0.8260193467140198, 0.8762916326522827, 0.9189026951789856, 0.9610784649848938, 1.1392977237701416], [-1.219455361366272, -0.62332683801651, 0.6973779797554016, -0.8171294331550598, 0.4345170855522156, 0.807735800743103, 0.977811872959137, 1.0264534950256348], [-0.9596766233444214, -0.14484058320522308, 0.5566535592079163, -0.7464998960494995, 0.548755407333374, 0.7815104722976685, 0.7932929992675781, 0.9520617723464966]]  # noqa: E501
    self.b_2 = [0.49179941415786743, -0.09761457145214081, -0.2935348153114319, 0.3233771026134491, -0.34799039363861084, -0.3518027067184448, -0.377750962972641, -0.4150520861148834]  # noqa: E501
    self.w_3 = [[-1.158638596534729, -2.490966320037842, -0.40622657537460327, 0.6911837458610535], [-0.10311989486217499, -0.5135303139686584, 0.9242042303085327, 0.6144431829452515], [0.5241267681121826, 0.7587763071060181, 0.49535948038101196, -0.11799097061157227], [-0.7598983645439148, -1.7621866464614868, -0.8218172192573547, 0.5069848895072937], [0.19491514563560486, 0.29965096712112427, 1.1732642650604248, 0.3333500027656555], [0.8625394701957703, 1.4422950744628906, 0.19079723954200745, -0.3177209198474884], [0.7915120720863342, 1.504770278930664, 0.26861780881881714, -0.07480443269014359], [0.9396238923072815, 1.9699760675430298, 0.38069552183151245, -0.2944820523262024]]  # noqa: E501
    self.b_3 = [-0.04122006520628929, -0.31427356600761414, -0.47199636697769165, 0.11220716685056686]
    self.w_4 = [[0.27233409881591797, -1.0532371997833252], [0.6921802759170532, 1.0548460483551025], [-0.08196081966161728, -1.8294554948806763], [0.15805041790008545, -0.9238361716270447]]  # noqa: E501
    self.b_4 = [-0.020527468994259834, -0.8144474625587463]

    self.input_norm_mat = np.array([[-3.0, 3.0], [-3.0, 3.0], [0.0, 40.0], [-3.0, 3.0]])
    self.output_norm_mat = np.array([-1.0, 1.0])
    self.temperature = temperature

  def sigmoid(self, x):
    return 1 / (1 + np.exp(-x))

  def forward(self, x):
    assert x.ndim == 1
    x = (x - self.input_norm_mat[:, 0]) / (self.input_norm_mat[:, 1] - self.input_norm_mat[:, 0])
    x = self.sigmoid(np.dot(x, self.w_1) + self.b_1)
    x = self.sigmoid(np.dot(x, self.w_2) + self.b_2)
    x = self.sigmoid(np.dot(x, self.w_3) + self.b_3)
    x = np.dot(x, self.w_4) + self.b_4
    return x

  def predict(self, x):
    x = self.forward(np.array(x))
    pred = np.random.laplace(x[0], np.exp(x[1]) / self.temperature)
    pred = pred * (self.output_norm_mat[1] - self.output_norm_mat[0]) + self.output_norm_mat[0]
    return float(pred)


class LatControlTorque(LatControl):
  def __init__(self, CP, CI):
    super().__init__(CP, CI)
    self.torque_params = CP.lateralTuning.torque
    self.pid = PIDController(self.torque_params.kp, self.torque_params.ki,
                             k_f=self.torque_params.kf, pos_limit=self.steer_max, neg_limit=-self.steer_max)
    self.torque_from_lateral_accel = CI.torque_from_lateral_accel()
    self.use_steering_angle = self.torque_params.useSteeringAngle
    self.steering_angle_deadzone_deg = self.torque_params.steeringAngleDeadzoneDeg
    self.ff_model = NanoFFModel(temperature=100.0)
    self.history = {key: deque([0, 0, 0], maxlen=3) for key in ["lataccel", "roll_compensation", "vego", "aego"]}
    self.history_counter = 0

  def update_live_torque_params(self, latAccelFactor, latAccelOffset, friction):
    self.torque_params.latAccelFactor = latAccelFactor
    self.torque_params.latAccelOffset = latAccelOffset
    self.torque_params.friction = friction

  def update(self, active, CS, VM, params, steer_limited, desired_curvature, llk):
    pid_log = log.ControlsState.LateralTorqueState.new_message()
    actual_curvature_vm = -VM.calc_curvature(math.radians(CS.steeringAngleDeg - params.angleOffsetDeg), CS.vEgo, params.roll)
    roll_compensation = math.sin(params.roll) * ACCELERATION_DUE_TO_GRAVITY

    if not active:
      output_torque = 0.0
      pid_log.active = False
    else:
      if self.use_steering_angle:
        actual_curvature = actual_curvature_vm
        # curvature_deadzone = abs(VM.calc_curvature(math.radians(self.steering_angle_deadzone_deg), CS.vEgo, 0.0))
      else:
        actual_curvature_llk = llk.angularVelocityCalibrated.value[2] / CS.vEgo
        actual_curvature = interp(CS.vEgo, [2.0, 5.0], [actual_curvature_vm, actual_curvature_llk])
        # curvature_deadzone = 0.0
      desired_lateral_accel = desired_curvature * CS.vEgo ** 2

      # desired rate is the desired rate of change in the setpoint, not the absolute desired curvature
      # desired_lateral_jerk = desired_curvature_rate * CS.vEgo ** 2
      actual_lateral_accel = actual_curvature * CS.vEgo ** 2

      low_speed_factor = interp(CS.vEgo, LOW_SPEED_X, LOW_SPEED_Y)**2
      setpoint = desired_lateral_accel + low_speed_factor * desired_curvature
      measurement = actual_lateral_accel + low_speed_factor * actual_curvature

      # lateral_accel_deadzone = curvature_deadzone * CS.vEgo ** 2
      # gravity_adjusted_lateral_accel = desired_lateral_accel - roll_compensation
      # torque_from_setpoint = self.torque_from_lateral_accel(setpoint, self.torque_params, setpoint,
      #                                                lateral_accel_deadzone, friction_compensation=False)
      # torque_from_measurement = self.torque_from_lateral_accel(measurement, self.torque_params, measurement,
      #                                                lateral_accel_deadzone, friction_compensation=False)
      # pid_log.error = torque_from_setpoint - torque_from_measurement
      # ff = self.torque_from_lateral_accel(gravity_adjusted_lateral_accel, self.torque_params,
      #                                     desired_lateral_accel - actual_lateral_accel,
      #                                     lateral_accel_deadzone, friction_compensation=True)

      state_vector = [roll_compensation, CS.vEgo, CS.aEgo]
      # history_state_vector = list(self.history["lataccel"]) + list(self.history["roll_compensation"]) + list(self.history["vego"]) + list(self.history["aego"])  # noqa: E501
      # torque_from_setpoint = self.ff_model.predict([setpoint] + state_vector + history_state_vector)
      # torque_from_measurement = self.ff_model.predict([measurement] + state_vector + history_state_vector)

      torque_from_setpoint = self.ff_model.predict([setpoint] + state_vector)
      torque_from_measurement = self.ff_model.predict([measurement] + state_vector)

      pid_log.error = torque_from_setpoint - torque_from_measurement
      # ff = self.ff_model.predict([desired_lateral_accel] + state_vector + history_state_vector)
      ff = self.ff_model.predict([desired_lateral_accel] + state_vector)

      friction = get_friction(pid_log.error, 0.0, 0.3, self.torque_params, True)
      ff += friction

      freeze_integrator = steer_limited or CS.steeringPressed or CS.vEgo < 5
      output_torque = self.pid.update(pid_log.error,
                                      feedforward=ff,
                                      speed=CS.vEgo,
                                      freeze_integrator=freeze_integrator)

      pid_log.active = True
      pid_log.p = self.pid.p
      pid_log.i = self.pid.i
      pid_log.d = self.pid.d
      pid_log.f = self.pid.f
      pid_log.output = -output_torque
      pid_log.actualLateralAccel = actual_lateral_accel
      pid_log.desiredLateralAccel = desired_lateral_accel
      pid_log.saturated = self._check_saturation(self.steer_max - abs(output_torque) < 1e-3, CS, steer_limited)

    if self.history_counter % 10 == 0:
      self.history["lataccel"].append(actual_curvature_vm * CS.vEgo ** 2)
      self.history["roll_compensation"].append(roll_compensation)
      self.history["vego"].append(CS.vEgo)
      self.history["aego"].append(CS.aEgo)

    self.history_counter = (self.history_counter + 1) % 10

    # TODO left is positive in this convention
    return -output_torque, 0.0, pid_log
