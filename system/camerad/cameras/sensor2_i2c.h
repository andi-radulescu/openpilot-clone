struct i2c_random_wr_payload start_reg_array_ar0231[] = {{0x301A, 0x91C}};
struct i2c_random_wr_payload stop_reg_array_ar0231[] = {{0x301A, 0x918}};
struct i2c_random_wr_payload start_reg_array_ox03c10[] = {{0x100, 1}};
struct i2c_random_wr_payload stop_reg_array_ox03c10[] = {{0x100, 0}};

struct i2c_random_wr_payload init_array_ox03c10[] = {
  {0x103, 1},
  {0x107, 1},

  // X3C_1920x1280_60fps_HDR4_LFR_PWL12_mipi1200

  // TPM
  {0x4d5a, 0x1a}, {0x4d09, 0xff}, {0x4d09, 0xdf},

  /*)
  // group 4
  {0x3208, 0x04},
  {0x4620, 0x04},
  {0x3208, 0x14},

  // group 5
  {0x3208, 0x05},
  {0x4620, 0x04},
  {0x3208, 0x15},

  // group 2
  {0x3208, 0x02},
  {0x3507, 0x00},
  {0x3208, 0x12},

  // delay launch group 2
  {0x3208, 0xa2},*/

  // PLL setup
  {0x0301, 0xc8}, // pll1_divs, pll1_predivp, pll1_divpix
  {0x0303, 0x01}, // pll1_prediv
  {0x0304, 0x01}, {0x0305, 0x2c}, // pll1_loopdiv = 300
  {0x0306, 0x04}, // pll1_divmipi = 4
  {0x0307, 0x01}, // pll1_divm = 1
  {0x0316, 0x00},
  {0x0317, 0x00},
  {0x0318, 0x00},
  {0x0323, 0x05}, // pll2_prediv
  {0x0324, 0x01}, {0x0325, 0x2c}, // pll2_divp = 300

  // SCLK/PCLK
  {0x0400, 0xe0}, {0x0401, 0x80},
  {0x0403, 0xde}, {0x0404, 0x34},
  {0x0405, 0x3b}, {0x0406, 0xde},
  {0x0407, 0x08},
  {0x0408, 0xe0}, {0x0409, 0x7f},
  {0x040a, 0xde}, {0x040b, 0x34},
  {0x040c, 0x47}, {0x040d, 0xd8},
  {0x040e, 0x08},

  // xchk
  {0x2803, 0xfe}, {0x280b, 0x00}, {0x280c, 0x79},

  // SC ctrl
  {0x3001, 0x03}, // io_pad_oen
  {0x3002, 0xf8}, // io_pad_oen
  {0x3005, 0x80}, // io_pad_out
  {0x3007, 0x01}, // io_pad_sel
  {0x3008, 0x80}, // io_pad_sel

  // FSIN first frame
  /*
  {0x3009, 0x2},
  {0x3015, 0x2},
  {0x3822, 0x20},
  {0x3823, 0x58},

  {0x3826, 0x0}, {0x3827, 0x8},
  {0x3881, 0x4},

  {0x3882, 0x8}, {0x3883, 0x0D},
  {0x3836, 0x1F}, {0x3837, 0x40},
  */

  // FSIN with external pulses
  {0x3009, 0x2},
  {0x3015, 0x2},
  {0x383E, 0x80},
  {0x3881, 0x4},
  {0x3882, 0x8}, {0x3883, 0x0D},
  {0x3836, 0x1F}, {0x3837, 0x40},

  {0x3012, 0x41}, // SC_PHY_CTRL = 4 lane MIPI
  {0x3020, 0x05}, // SC_CTRL_20

  // this is not in the datasheet, listed as RSVD
  // but the camera doesn't work without it
  {0x3700, 0x28}, {0x3701, 0x15}, {0x3702, 0x19}, {0x3703, 0x23},
  {0x3704, 0x0a}, {0x3705, 0x00}, {0x3706, 0x3e}, {0x3707, 0x0d},
  {0x3708, 0x50}, {0x3709, 0x5a}, {0x370a, 0x00}, {0x370b, 0x96},
  {0x3711, 0x11}, {0x3712, 0x13}, {0x3717, 0x02}, {0x3718, 0x73},
  {0x372c, 0x40}, {0x3733, 0x01}, {0x3738, 0x36}, {0x3739, 0x36},
  {0x373a, 0x25}, {0x373b, 0x25}, {0x373f, 0x21}, {0x3740, 0x21},
  {0x3741, 0x21}, {0x3742, 0x21}, {0x3747, 0x28}, {0x3748, 0x28},
  {0x3749, 0x19}, {0x3755, 0x1a}, {0x3756, 0x0a}, {0x3757, 0x1c},
  {0x3765, 0x19}, {0x3766, 0x05}, {0x3767, 0x05}, {0x3768, 0x13},
  {0x376c, 0x07}, {0x3778, 0x20}, {0x377c, 0xc8}, {0x3781, 0x02},
  {0x3783, 0x02}, {0x379c, 0x58}, {0x379e, 0x00}, {0x379f, 0x00},
  {0x37a0, 0x00}, {0x37bc, 0x22}, {0x37c0, 0x01}, {0x37c4, 0x3e},
  {0x37c5, 0x3e}, {0x37c6, 0x2a}, {0x37c7, 0x28}, {0x37c8, 0x02},
  {0x37c9, 0x12}, {0x37cb, 0x29}, {0x37cd, 0x29}, {0x37d2, 0x00},
  {0x37d3, 0x73}, {0x37d6, 0x00}, {0x37d7, 0x6b}, {0x37dc, 0x00},
  {0x37df, 0x54}, {0x37e2, 0x00}, {0x37e3, 0x00}, {0x37f8, 0x00},
  {0x37f9, 0x01}, {0x37fa, 0x00}, {0x37fb, 0x19},

  // also RSVD
  {0x3c03, 0x01}, {0x3c04, 0x01}, {0x3c06, 0x21}, {0x3c08, 0x01},
  {0x3c09, 0x01}, {0x3c0a, 0x01}, {0x3c0b, 0x21}, {0x3c13, 0x21},
  {0x3c14, 0x82}, {0x3c16, 0x13}, {0x3c21, 0x00}, {0x3c22, 0xf3},
  {0x3c37, 0x12}, {0x3c38, 0x31}, {0x3c3c, 0x00}, {0x3c3d, 0x03},
  {0x3c44, 0x16}, {0x3c5c, 0x8a}, {0x3c5f, 0x03}, {0x3c61, 0x80},
  {0x3c6f, 0x2b}, {0x3c70, 0x5f}, {0x3c71, 0x2c}, {0x3c72, 0x2c},
  {0x3c73, 0x2c}, {0x3c76, 0x12},

  // PEC checks
  {0x3182, 0x12},

  {0x320e, 0x00}, {0x320f, 0x00}, // RSVD
  {0x3211, 0x61},
  {0x3215, 0xcd},
  {0x3219, 0x08},

  {0x3506, 0x20}, {0x3507, 0x00}, // hcg fine exposure
  {0x350a, 0x04}, {0x350b, 0x00}, {0x350c, 0x00}, // hcg digital gain

  {0x3586, 0x40}, {0x3587, 0x00}, // lcg fine exposure
  {0x358a, 0x04}, {0x358b, 0x00}, {0x358c, 0x00}, // lcg digital gain

  {0x3546, 0x20}, {0x3547, 0x00}, // spd fine exposure
  {0x354a, 0x04}, {0x354b, 0x00}, {0x354c, 0x00}, // spd digital gain

  {0x35c6, 0xb0}, {0x35c7, 0x00}, // vs fine exposure
  {0x35ca, 0x04}, {0x35cb, 0x00}, {0x35cc, 0x00}, // vs digital gain

  // also RSVD
  {0x3600, 0x8f}, {0x3605, 0x16}, {0x3609, 0xf0}, {0x360a, 0x01},
  {0x360e, 0x1d}, {0x360f, 0x10}, {0x3610, 0x70}, {0x3611, 0x3a},
  {0x3612, 0x28}, {0x361a, 0x29}, {0x361b, 0x6c}, {0x361c, 0x0b},
  {0x361d, 0x00}, {0x361e, 0xfc}, {0x362a, 0x00}, {0x364d, 0x0f},
  {0x364e, 0x18}, {0x364f, 0x12}, {0x3653, 0x1c}, {0x3654, 0x00},
  {0x3655, 0x1f}, {0x3656, 0x1f}, {0x3657, 0x0c}, {0x3658, 0x0a},
  {0x3659, 0x14}, {0x365a, 0x18}, {0x365b, 0x14}, {0x365c, 0x10},
  {0x365e, 0x12}, {0x3674, 0x08}, {0x3677, 0x3a}, {0x3678, 0x3a},
  {0x3679, 0x19},

  // Y_ADDR_START = 4
  {0x3802, 0x00}, {0x3803, 0x04},
  // Y_ADDR_END = 0x50b
  {0x3806, 0x05}, {0x3807, 0x0b},

  // X_OUTPUT_SIZE = 0x780 = 1920 (changed to 1928)
  {0x3808, 0x07}, {0x3809, 0x88},

  // Y_OUTPUT_SIZE = 0x500 = 1280 (changed to 1208)
  {0x380a, 0x04}, {0x380b, 0xb8},

  // horizontal timing 0x447
  {0x380c, 0x04}, {0x380d, 0x47},

  // rows per frame (was 0x2ae)
  // 0x8ae = 53.65 ms
  {0x380e, 0x08}, {0x380f, 0x15},
  // this should be triggered by FSIN, not free running

  {0x3810, 0x00}, {0x3811, 0x08}, // x cutoff
  {0x3812, 0x00}, {0x3813, 0x04}, // y cutoff
  {0x3816, 0x01},
  {0x3817, 0x01},
  {0x381c, 0x18},
  {0x381e, 0x01},
  {0x381f, 0x01},

  // don't mirror, just flip
  {0x3820, 0x04},

  {0x3821, 0x19},
  {0x3832, 0x00},
  {0x3834, 0x00},
  {0x384c, 0x02},
  {0x384d, 0x0d},
  {0x3850, 0x00},
  {0x3851, 0x42},
  {0x3852, 0x00},
  {0x3853, 0x40},
  {0x3858, 0x04},
  {0x388c, 0x02},
  {0x388d, 0x2b},

  // APC
  {0x3b40, 0x05}, {0x3b41, 0x40}, {0x3b42, 0x00}, {0x3b43, 0x90},
  {0x3b44, 0x00}, {0x3b45, 0x20}, {0x3b46, 0x00}, {0x3b47, 0x20},
  {0x3b48, 0x19}, {0x3b49, 0x12}, {0x3b4a, 0x16}, {0x3b4b, 0x2e},
  {0x3b4c, 0x00}, {0x3b4d, 0x00},
  {0x3b86, 0x00}, {0x3b87, 0x34}, {0x3b88, 0x00}, {0x3b89, 0x08},
  {0x3b8a, 0x05}, {0x3b8b, 0x00}, {0x3b8c, 0x07}, {0x3b8d, 0x80},
  {0x3b8e, 0x00}, {0x3b8f, 0x00}, {0x3b92, 0x05}, {0x3b93, 0x00},
  {0x3b94, 0x07}, {0x3b95, 0x80}, {0x3b9e, 0x09},

  // OTP
  {0x3d82, 0x73},
  {0x3d85, 0x05},
  {0x3d8a, 0x03},
  {0x3d8b, 0xff},
  {0x3d99, 0x00},
  {0x3d9a, 0x9f},
  {0x3d9b, 0x00},
  {0x3d9c, 0xa0},
  {0x3da4, 0x00},
  {0x3da7, 0x50},

  // DTR
  {0x420e, 0x6b},
  {0x420f, 0x6e},
  {0x4210, 0x06},
  {0x4211, 0xc1},
  {0x421e, 0x02},
  {0x421f, 0x45},
  {0x4220, 0xe1},
  {0x4221, 0x01},
  {0x4301, 0xff},
  {0x4307, 0x03},
  {0x4308, 0x13},
  {0x430a, 0x13},
  {0x430d, 0x93},
  {0x430f, 0x57},
  {0x4310, 0x95},
  {0x4311, 0x16},
  {0x4316, 0x00},

  {0x4317, 0x38}, // both embedded rows are enabled

  {0x4319, 0x03}, // spd dcg
  {0x431a, 0x00}, // 8 bit mipi
  {0x431b, 0x00},
  {0x431d, 0x2a},
  {0x431e, 0x11},

  {0x431f, 0x20}, // enable PWL (pwl0_en), 12 bits
  //{0x431f, 0x00}, // disable PWL

  {0x4320, 0x19},
  {0x4323, 0x80},
  {0x4324, 0x00},
  {0x4503, 0x4e},
  {0x4505, 0x00},
  {0x4509, 0x00},
  {0x450a, 0x00},
  {0x4580, 0xf8},
  {0x4583, 0x07},
  {0x4584, 0x6a},
  {0x4585, 0x08},
  {0x4586, 0x05},
  {0x4587, 0x04},
  {0x4588, 0x73},
  {0x4589, 0x05},
  {0x458a, 0x1f},
  {0x458b, 0x02},
  {0x458c, 0xdc},
  {0x458d, 0x03},
  {0x458e, 0x02},
  {0x4597, 0x07},
  {0x4598, 0x40},
  {0x4599, 0x0e},
  {0x459a, 0x0e},
  {0x459b, 0xfb},
  {0x459c, 0xf3},
  {0x4602, 0x00},
  {0x4603, 0x13},
  {0x4604, 0x00},
  {0x4609, 0x0a},
  {0x460a, 0x30},
  {0x4610, 0x00},
  {0x4611, 0x70},
  {0x4612, 0x01},
  {0x4613, 0x00},
  {0x4614, 0x00},
  {0x4615, 0x70},
  {0x4616, 0x01},
  {0x4617, 0x00},

  {0x4800, 0x04}, // invert output PCLK
  {0x480a, 0x22},
  {0x4813, 0xe4},

  // mipi
  {0x4814, 0x2a},
  {0x4837, 0x0d},
  {0x484b, 0x47},
  {0x484f, 0x00},
  {0x4887, 0x51},
  {0x4d00, 0x4a},
  {0x4d01, 0x18},
  {0x4d05, 0xff},
  {0x4d06, 0x88},
  {0x4d08, 0x63},
  {0x4d09, 0xdf},
  {0x4d15, 0x7d},
  {0x4d1a, 0x20},
  {0x4d30, 0x0a},
  {0x4d31, 0x00},
  {0x4d34, 0x7d},
  {0x4d3c, 0x7d},
  {0x4f00, 0x00},
  {0x4f01, 0x00},
  {0x4f02, 0x00},
  {0x4f03, 0x20},
  {0x4f04, 0xe0},
  {0x6a00, 0x00},
  {0x6a01, 0x20},
  {0x6a02, 0x00},
  {0x6a03, 0x20},
  {0x6a04, 0x02},
  {0x6a05, 0x80},
  {0x6a06, 0x01},
  {0x6a07, 0xe0},
  {0x6a08, 0xcf},
  {0x6a09, 0x01},
  {0x6a0a, 0x40},
  {0x6a20, 0x00},
  {0x6a21, 0x02},
  {0x6a22, 0x00},
  {0x6a23, 0x00},
  {0x6a24, 0x00},
  {0x6a25, 0x00},
  {0x6a26, 0x00},
  {0x6a27, 0x00},
  {0x6a28, 0x00},

  // isp
  {0x5000, 0x8f},
  {0x5001, 0x75},
  {0x5002, 0x7f}, // PWL0
  //{0x5002, 0x3f}, // PWL disable
  {0x5003, 0x7a},

  {0x5004, 0x3e},
  {0x5005, 0x1e},
  {0x5006, 0x1e},
  {0x5007, 0x1e},

  {0x5008, 0x00},
  {0x500c, 0x00},
  {0x502c, 0x00},
  {0x502e, 0x00},
  {0x502f, 0x00},
  {0x504b, 0x00},
  {0x5053, 0x00},
  {0x505b, 0x00},
  {0x5063, 0x00},
  {0x5070, 0x00},
  {0x5074, 0x04},
  {0x507a, 0x04},
  {0x507b, 0x09},
  {0x5500, 0x02},
  {0x5700, 0x02},
  {0x5900, 0x02},
  {0x6007, 0x04},
  {0x6008, 0x05},
  {0x6009, 0x02},
  {0x600b, 0x08},
  {0x600c, 0x07},
  {0x600d, 0x88},
  {0x6016, 0x00},
  {0x6027, 0x04},
  {0x6028, 0x05},
  {0x6029, 0x02},
  {0x602b, 0x08},
  {0x602c, 0x07},
  {0x602d, 0x88},
  {0x6047, 0x04},
  {0x6048, 0x05},
  {0x6049, 0x02},
  {0x604b, 0x08},
  {0x604c, 0x07},
  {0x604d, 0x88},
  {0x6067, 0x04},
  {0x6068, 0x05},
  {0x6069, 0x02},
  {0x606b, 0x08},
  {0x606c, 0x07},
  {0x606d, 0x88},
  {0x6087, 0x04},
  {0x6088, 0x05},
  {0x6089, 0x02},
  {0x608b, 0x08},
  {0x608c, 0x07},
  {0x608d, 0x88},

  // 12-bit PWL0
  {0x5e00, 0x00},

  // m_ndX_exp[0:32]
  // 9*2+0xa*3+0xb*2+0xc*2+0xd*2+0xe*2+0xf*2+0x10*2+0x11*2+0x12*4+0x13*3+0x14*3+0x15*3+0x16 = 518
  {0x5e01, 0x09},
  {0x5e02, 0x09},
  {0x5e03, 0x0a},
  {0x5e04, 0x0a},
  {0x5e05, 0x0a},
  {0x5e06, 0x0b},
  {0x5e07, 0x0b},
  {0x5e08, 0x0c},
  {0x5e09, 0x0c},
  {0x5e0a, 0x0d},
  {0x5e0b, 0x0d},
  {0x5e0c, 0x0e},
  {0x5e0d, 0x0e},
  {0x5e0e, 0x0f},
  {0x5e0f, 0x0f},
  {0x5e10, 0x10},
  {0x5e11, 0x10},
  {0x5e12, 0x11},
  {0x5e13, 0x11},
  {0x5e14, 0x12},
  {0x5e15, 0x12},
  {0x5e16, 0x12},
  {0x5e17, 0x12},
  {0x5e18, 0x13},
  {0x5e19, 0x13},
  {0x5e1a, 0x13},
  {0x5e1b, 0x14},
  {0x5e1c, 0x14},
  {0x5e1d, 0x14},
  {0x5e1e, 0x15},
  {0x5e1f, 0x15},
  {0x5e20, 0x15},
  {0x5e21, 0x16},

  // m_ndY_val[0:32]
  // 0x200+0xff+0x100*3+0x80*12+0x40*16 = 4095
  {0x5e22, 0x00}, {0x5e23, 0x02}, {0x5e24, 0x00},
  {0x5e25, 0x00}, {0x5e26, 0x00}, {0x5e27, 0xff},
  {0x5e28, 0x00}, {0x5e29, 0x01}, {0x5e2a, 0x00},
  {0x5e2b, 0x00}, {0x5e2c, 0x01}, {0x5e2d, 0x00},
  {0x5e2e, 0x00}, {0x5e2f, 0x01}, {0x5e30, 0x00},
  {0x5e31, 0x00}, {0x5e32, 0x00}, {0x5e33, 0x80},
  {0x5e34, 0x00}, {0x5e35, 0x00}, {0x5e36, 0x80},
  {0x5e37, 0x00}, {0x5e38, 0x00}, {0x5e39, 0x80},
  {0x5e3a, 0x00}, {0x5e3b, 0x00}, {0x5e3c, 0x80},
  {0x5e3d, 0x00}, {0x5e3e, 0x00}, {0x5e3f, 0x80},
  {0x5e40, 0x00}, {0x5e41, 0x00}, {0x5e42, 0x80},
  {0x5e43, 0x00}, {0x5e44, 0x00}, {0x5e45, 0x80},
  {0x5e46, 0x00}, {0x5e47, 0x00}, {0x5e48, 0x80},
  {0x5e49, 0x00}, {0x5e4a, 0x00}, {0x5e4b, 0x80},
  {0x5e4c, 0x00}, {0x5e4d, 0x00}, {0x5e4e, 0x80},
  {0x5e4f, 0x00}, {0x5e50, 0x00}, {0x5e51, 0x80},
  {0x5e52, 0x00}, {0x5e53, 0x00}, {0x5e54, 0x80},
  {0x5e55, 0x00}, {0x5e56, 0x00}, {0x5e57, 0x40},
  {0x5e58, 0x00}, {0x5e59, 0x00}, {0x5e5a, 0x40},
  {0x5e5b, 0x00}, {0x5e5c, 0x00}, {0x5e5d, 0x40},
  {0x5e5e, 0x00}, {0x5e5f, 0x00}, {0x5e60, 0x40},
  {0x5e61, 0x00}, {0x5e62, 0x00}, {0x5e63, 0x40},
  {0x5e64, 0x00}, {0x5e65, 0x00}, {0x5e66, 0x40},
  {0x5e67, 0x00}, {0x5e68, 0x00}, {0x5e69, 0x40},
  {0x5e6a, 0x00}, {0x5e6b, 0x00}, {0x5e6c, 0x40},
  {0x5e6d, 0x00}, {0x5e6e, 0x00}, {0x5e6f, 0x40},
  {0x5e70, 0x00}, {0x5e71, 0x00}, {0x5e72, 0x40},
  {0x5e73, 0x00}, {0x5e74, 0x00}, {0x5e75, 0x40},
  {0x5e76, 0x00}, {0x5e77, 0x00}, {0x5e78, 0x40},
  {0x5e79, 0x00}, {0x5e7a, 0x00}, {0x5e7b, 0x40},
  {0x5e7c, 0x00}, {0x5e7d, 0x00}, {0x5e7e, 0x40},
  {0x5e7f, 0x00}, {0x5e80, 0x00}, {0x5e81, 0x40},
  {0x5e82, 0x00}, {0x5e83, 0x00}, {0x5e84, 0x40},

  // disable PWL
  /*{0x5e01, 0x18}, {0x5e02, 0x00}, {0x5e03, 0x00}, {0x5e04, 0x00},
  {0x5e05, 0x00}, {0x5e06, 0x00}, {0x5e07, 0x00}, {0x5e08, 0x00},
  {0x5e09, 0x00}, {0x5e0a, 0x00}, {0x5e0b, 0x00}, {0x5e0c, 0x00},
  {0x5e0d, 0x00}, {0x5e0e, 0x00}, {0x5e0f, 0x00}, {0x5e10, 0x00},
  {0x5e11, 0x00}, {0x5e12, 0x00}, {0x5e13, 0x00}, {0x5e14, 0x00},
  {0x5e15, 0x00}, {0x5e16, 0x00}, {0x5e17, 0x00}, {0x5e18, 0x00},
  {0x5e19, 0x00}, {0x5e1a, 0x00}, {0x5e1b, 0x00}, {0x5e1c, 0x00},
  {0x5e1d, 0x00}, {0x5e1e, 0x00}, {0x5e1f, 0x00}, {0x5e20, 0x00},
  {0x5e21, 0x00},

  {0x5e22, 0x00}, {0x5e23, 0x0f}, {0x5e24, 0xFF},*/

  {0x4001, 0x2b},  // BLC_CTRL_1
  {0x4008, 0x02}, {0x4009, 0x03},
  {0x4018, 0x12},
  {0x4022, 0x40},
  {0x4023, 0x20},

  // all black level targets are 0x40
  {0x4026, 0x00}, {0x4027, 0x40},
  {0x4028, 0x00}, {0x4029, 0x40},
  {0x402a, 0x00}, {0x402b, 0x40},
  {0x402c, 0x00}, {0x402d, 0x40},

  {0x407e, 0xcc},
  {0x407f, 0x18},
  {0x4080, 0xff},
  {0x4081, 0xff},
  {0x4082, 0x01},
  {0x4083, 0x53},
  {0x4084, 0x01},
  {0x4085, 0x2b},
  {0x4086, 0x00},
  {0x4087, 0xb3},

  {0x4640, 0x40},
  {0x4641, 0x11},
  {0x4642, 0x0e},
  {0x4643, 0xee},
  {0x4646, 0x0f},
  {0x4648, 0x00},
  {0x4649, 0x03},

  {0x4f00, 0x00},
  {0x4f01, 0x00},
  {0x4f02, 0x80},
  {0x4f03, 0x2c},
  {0x4f04, 0xf8},

  {0x4d09, 0xff},
  {0x4d09, 0xdf},

  {0x5003, 0x7a},
  {0x5b80, 0x08},
  {0x5c00, 0x08},
  {0x5c80, 0x00},
  {0x5bbe, 0x12},
  {0x5c3e, 0x12},
  {0x5cbe, 0x12},
  {0x5b8a, 0x80},
  {0x5b8b, 0x80},
  {0x5b8c, 0x80},
  {0x5b8d, 0x80},
  {0x5b8e, 0x60},
  {0x5b8f, 0x80},
  {0x5b90, 0x80},
  {0x5b91, 0x80},
  {0x5b92, 0x80},
  {0x5b93, 0x20},
  {0x5b94, 0x80},
  {0x5b95, 0x80},
  {0x5b96, 0x80},
  {0x5b97, 0x20},
  {0x5b98, 0x00},
  {0x5b99, 0x80},
  {0x5b9a, 0x40},
  {0x5b9b, 0x20},
  {0x5b9c, 0x00},
  {0x5b9d, 0x00},
  {0x5b9e, 0x80},
  {0x5b9f, 0x00},
  {0x5ba0, 0x00},
  {0x5ba1, 0x00},
  {0x5ba2, 0x00},
  {0x5ba3, 0x00},
  {0x5ba4, 0x00},
  {0x5ba5, 0x00},
  {0x5ba6, 0x00},
  {0x5ba7, 0x00},
  {0x5ba8, 0x02},
  {0x5ba9, 0x00},
  {0x5baa, 0x02},
  {0x5bab, 0x76},
  {0x5bac, 0x03},
  {0x5bad, 0x08},
  {0x5bae, 0x00},
  {0x5baf, 0x80},
  {0x5bb0, 0x00},
  {0x5bb1, 0xc0},
  {0x5bb2, 0x01},
  {0x5bb3, 0x00},

  // m_nNormCombineWeight
  {0x5c0a, 0x80}, {0x5c0b, 0x80}, {0x5c0c, 0x80}, {0x5c0d, 0x80}, {0x5c0e, 0x60},
  {0x5c0f, 0x80}, {0x5c10, 0x80}, {0x5c11, 0x80}, {0x5c12, 0x60}, {0x5c13, 0x20},
  {0x5c14, 0x80}, {0x5c15, 0x80}, {0x5c16, 0x80}, {0x5c17, 0x20}, {0x5c18, 0x00},
  {0x5c19, 0x80}, {0x5c1a, 0x40}, {0x5c1b, 0x20}, {0x5c1c, 0x00}, {0x5c1d, 0x00},
  {0x5c1e, 0x80}, {0x5c1f, 0x00}, {0x5c20, 0x00}, {0x5c21, 0x00}, {0x5c22, 0x00},
  {0x5c23, 0x00}, {0x5c24, 0x00}, {0x5c25, 0x00}, {0x5c26, 0x00}, {0x5c27, 0x00},

  // m_nCombinThreL
  {0x5c28, 0x02}, {0x5c29, 0x00},
  {0x5c2a, 0x02}, {0x5c2b, 0x76},
  {0x5c2c, 0x03}, {0x5c2d, 0x08},

  // m_nCombinThreS
  {0x5c2e, 0x00}, {0x5c2f, 0x80},
  {0x5c30, 0x00}, {0x5c31, 0xc0},
  {0x5c32, 0x01}, {0x5c33, 0x00},

  // m_nNormCombineWeight
  {0x5c8a, 0x80}, {0x5c8b, 0x80}, {0x5c8c, 0x80}, {0x5c8d, 0x80}, {0x5c8e, 0x80},
  {0x5c8f, 0x80}, {0x5c90, 0x80}, {0x5c91, 0x80}, {0x5c92, 0x80}, {0x5c93, 0x60},
  {0x5c94, 0x80}, {0x5c95, 0x80}, {0x5c96, 0x80}, {0x5c97, 0x60}, {0x5c98, 0x40},
  {0x5c99, 0x80}, {0x5c9a, 0x80}, {0x5c9b, 0x80}, {0x5c9c, 0x40}, {0x5c9d, 0x00},
  {0x5c9e, 0x80}, {0x5c9f, 0x80}, {0x5ca0, 0x80}, {0x5ca1, 0x20}, {0x5ca2, 0x00},
  {0x5ca3, 0x80}, {0x5ca4, 0x80}, {0x5ca5, 0x00}, {0x5ca6, 0x00}, {0x5ca7, 0x00},

  {0x5ca8, 0x01}, {0x5ca9, 0x00},
  {0x5caa, 0x02}, {0x5cab, 0x00},
  {0x5cac, 0x03}, {0x5cad, 0x08},

  {0x5cae, 0x01}, {0x5caf, 0x00},
  {0x5cb0, 0x02}, {0x5cb1, 0x00},
  {0x5cb2, 0x03}, {0x5cb3, 0x08},

  // combine ISP
  {0x5be7, 0x80},
  {0x5bc9, 0x80},
  {0x5bca, 0x80},
  {0x5bcb, 0x80},
  {0x5bcc, 0x80},
  {0x5bcd, 0x80},
  {0x5bce, 0x80},
  {0x5bcf, 0x80},
  {0x5bd0, 0x80},
  {0x5bd1, 0x80},
  {0x5bd2, 0x20},
  {0x5bd3, 0x80},
  {0x5bd4, 0x40},
  {0x5bd5, 0x20},
  {0x5bd6, 0x00},
  {0x5bd7, 0x00},
  {0x5bd8, 0x00},
  {0x5bd9, 0x00},
  {0x5bda, 0x00},
  {0x5bdb, 0x00},
  {0x5bdc, 0x00},
  {0x5bdd, 0x00},
  {0x5bde, 0x00},
  {0x5bdf, 0x00},
  {0x5be0, 0x00},
  {0x5be1, 0x00},
  {0x5be2, 0x00},
  {0x5be3, 0x00},
  {0x5be4, 0x00},
  {0x5be5, 0x00},
  {0x5be6, 0x00},

  // m_nSPDCombineWeight
  {0x5c49, 0x80}, {0x5c4a, 0x80}, {0x5c4b, 0x80}, {0x5c4c, 0x80}, {0x5c4d, 0x40},
  {0x5c4e, 0x80}, {0x5c4f, 0x80}, {0x5c50, 0x80}, {0x5c51, 0x60}, {0x5c52, 0x20},
  {0x5c53, 0x80}, {0x5c54, 0x80}, {0x5c55, 0x80}, {0x5c56, 0x20}, {0x5c57, 0x00},
  {0x5c58, 0x80}, {0x5c59, 0x40}, {0x5c5a, 0x20}, {0x5c5b, 0x00}, {0x5c5c, 0x00},
  {0x5c5d, 0x80}, {0x5c5e, 0x00}, {0x5c5f, 0x00}, {0x5c60, 0x00}, {0x5c61, 0x00},
  {0x5c62, 0x00}, {0x5c63, 0x00}, {0x5c64, 0x00}, {0x5c65, 0x00}, {0x5c66, 0x00},

  // m_nSPDCombineWeight
  {0x5cc9, 0x80}, {0x5cca, 0x80}, {0x5ccb, 0x80}, {0x5ccc, 0x80}, {0x5ccd, 0x80},
  {0x5cce, 0x80}, {0x5ccf, 0x80}, {0x5cd0, 0x80}, {0x5cd1, 0x80}, {0x5cd2, 0x60},
  {0x5cd3, 0x80}, {0x5cd4, 0x80}, {0x5cd5, 0x80}, {0x5cd6, 0x60}, {0x5cd7, 0x40},
  {0x5cd8, 0x80}, {0x5cd9, 0x80}, {0x5cda, 0x80}, {0x5cdb, 0x40}, {0x5cdc, 0x20},
  {0x5cdd, 0x80}, {0x5cde, 0x80}, {0x5cdf, 0x80}, {0x5ce0, 0x20}, {0x5ce1, 0x00},
  {0x5ce2, 0x80}, {0x5ce3, 0x80}, {0x5ce4, 0x80}, {0x5ce5, 0x00}, {0x5ce6, 0x00},

  {0x5d74, 0x01},
  {0x5d75, 0x00},

  {0x5d1f, 0x81},
  {0x5d11, 0x00},
  {0x5d12, 0x10},
  {0x5d13, 0x10},
  {0x5d15, 0x05},
  {0x5d16, 0x05},
  {0x5d17, 0x05},
  {0x5d08, 0x03},
  {0x5d09, 0xb6},
  {0x5d0a, 0x03},
  {0x5d0b, 0xb6},
  {0x5d18, 0x03},
  {0x5d19, 0xb6},
  {0x5d62, 0x01},
  {0x5d40, 0x02},
  {0x5d41, 0x01},
  {0x5d63, 0x1f},
  {0x5d64, 0x00},
  {0x5d65, 0x80},
  {0x5d56, 0x00},
  {0x5d57, 0x20},
  {0x5d58, 0x00},
  {0x5d59, 0x20},
  {0x5d5a, 0x00},
  {0x5d5b, 0x0c},
  {0x5d5c, 0x02},
  {0x5d5d, 0x40},
  {0x5d5e, 0x02},
  {0x5d5f, 0x40},
  {0x5d60, 0x03},
  {0x5d61, 0x40},
  {0x5d4a, 0x02},
  {0x5d4b, 0x40},
  {0x5d4c, 0x02},
  {0x5d4d, 0x40},
  {0x5d4e, 0x02},
  {0x5d4f, 0x40},
  {0x5d50, 0x18},
  {0x5d51, 0x80},
  {0x5d52, 0x18},
  {0x5d53, 0x80},
  {0x5d54, 0x18},
  {0x5d55, 0x80},
  {0x5d46, 0x20},
  {0x5d47, 0x00},
  {0x5d48, 0x22},
  {0x5d49, 0x00},
  {0x5d42, 0x20},
  {0x5d43, 0x00},
  {0x5d44, 0x22},
  {0x5d45, 0x00},

  {0x5004, 0x1e},
  {0x4221, 0x03},  // this is changed from 1 -> 3

  // DCG exposure coarse
  {0x3501, 0x01}, {0x3502, 0xc8},
  // SPD exposure coarse
  {0x3541, 0x01}, {0x3542, 0xc8},
  // VS exposure coarse
  {0x35c1, 0x00}, {0x35c2, 0x01},

  // crc reference
  {0x420e, 0x66}, {0x420f, 0x5d}, {0x4210, 0xa8}, {0x4211, 0x55},
  // crc stat check
  {0x507a, 0x5f}, {0x507b, 0x46},

  // watchdog control
  {0x4f00, 0x00}, {0x4f01, 0x01}, {0x4f02, 0x80}, {0x4f04, 0x2c},

  // color balance gains
  // blue
  {0x5280, 0x06}, {0x5281, 0x4A}, // hcg
  {0x5480, 0x06}, {0x5481, 0x4A}, // lcg
  {0x5680, 0x07}, {0x5681, 0xDD}, // spd
  {0x5880, 0x06}, {0x5881, 0x4A}, // vs

  // green(blue)
  {0x5282, 0x04}, {0x5283, 0x00},
  {0x5482, 0x04}, {0x5483, 0x00},
  {0x5682, 0x04}, {0x5683, 0x00},
  {0x5882, 0x04}, {0x5883, 0x00},

  // green(red)
  {0x5284, 0x04}, {0x5285, 0x00},
  {0x5484, 0x04}, {0x5485, 0x00},
  {0x5684, 0x04}, {0x5685, 0x00},
  {0x5884, 0x04}, {0x5885, 0x00},

  // red
  {0x5286, 0x08}, {0x5287, 0x6C},
  {0x5486, 0x08}, {0x5487, 0x6C},
  {0x5686, 0x08}, {0x5687, 0xAA},
  {0x5886, 0x08}, {0x5887, 0x6C},
};

struct i2c_random_wr_payload init_array_ar0231[] = {
  {0x301A, 0x0018}, // RESET_REGISTER

  // CLOCK Settings
  // input clock is 19.2 / 2 * 0x37 = 528 MHz
  // pixclk is 528 / 6 = 88 MHz
  // full roll time is 1000/(PIXCLK/(LINE_LENGTH_PCK*FRAME_LENGTH_LINES)) = 39.99 ms
  // img  roll time is 1000/(PIXCLK/(LINE_LENGTH_PCK*Y_OUTPUT_CONTROL))   = 22.85 ms
  {0x302A, 0x0006}, // VT_PIX_CLK_DIV
  {0x302C, 0x0001}, // VT_SYS_CLK_DIV
  {0x302E, 0x0002}, // PRE_PLL_CLK_DIV
  {0x3030, 0x0037}, // PLL_MULTIPLIER
  {0x3036, 0x000C}, // OP_PIX_CLK_DIV
  {0x3038, 0x0001}, // OP_SYS_CLK_DIV

  // FORMAT
  {0x3040, 0xC000}, // READ_MODE
  {0x3004, 0x0000}, // X_ADDR_START_
  {0x3008, 0x0787}, // X_ADDR_END_
  {0x3002, 0x0000}, // Y_ADDR_START_
  {0x3006, 0x04B7}, // Y_ADDR_END_
  {0x3032, 0x0000}, // SCALING_MODE
  {0x30A2, 0x0001}, // X_ODD_INC_
  {0x30A6, 0x0001}, // Y_ODD_INC_
  {0x3402, 0x0788}, // X_OUTPUT_CONTROL
  {0x3404, 0x04B8}, // Y_OUTPUT_CONTROL
  {0x3064, 0x1982}, // SMIA_TEST
  {0x30BA, 0x11F2}, // DIGITAL_CTRL

  // Enable external trigger and disable GPIO outputs
  {0x30CE, 0x0120}, // SLAVE_SH_SYNC_MODE | FRAME_START_MODE
  {0x340A, 0xE0},   // GPIO3_INPUT_DISABLE | GPIO2_INPUT_DISABLE | GPIO1_INPUT_DISABLE
  {0x340C, 0x802},  // GPIO_HIDRV_EN | GPIO0_ISEL=2

  // Readout timing
  {0x300C, 0x0672}, // LINE_LENGTH_PCK (valid for 3-exposure HDR)
  {0x300A, 0x0855}, // FRAME_LENGTH_LINES
  {0x3042, 0x0000}, // EXTRA_DELAY

  // Readout Settings
  {0x31AE, 0x0204}, // SERIAL_FORMAT, 4-lane MIPI
  {0x31AC, 0x0C0C}, // DATA_FORMAT_BITS, 12 -> 12
  {0x3342, 0x1212}, // MIPI_F1_PDT_EDT
  {0x3346, 0x1212}, // MIPI_F2_PDT_EDT
  {0x334A, 0x1212}, // MIPI_F3_PDT_EDT
  {0x334E, 0x1212}, // MIPI_F4_PDT_EDT
  {0x3344, 0x0011}, // MIPI_F1_VDT_VC
  {0x3348, 0x0111}, // MIPI_F2_VDT_VC
  {0x334C, 0x0211}, // MIPI_F3_VDT_VC
  {0x3350, 0x0311}, // MIPI_F4_VDT_VC
  {0x31B0, 0x0053}, // FRAME_PREAMBLE
  {0x31B2, 0x003B}, // LINE_PREAMBLE
  {0x301A, 0x001C}, // RESET_REGISTER

  // Noise Corrections
  {0x3092, 0x0C24}, // ROW_NOISE_CONTROL
  {0x337A, 0x0C80}, // DBLC_SCALE0
  {0x3370, 0x03B1}, // DBLC
  {0x3044, 0x0400}, // DARK_CONTROL

  // Enable temperature sensor
  {0x30B4, 0x0007}, // TEMPSENS0_CTRL_REG
  {0x30B8, 0x0007}, // TEMPSENS1_CTRL_REG

  // Enable dead pixel correction using
  // the 1D line correction scheme
  {0x31E0, 0x0003},

  // HDR Settings
  {0x3082, 0x0004}, // OPERATION_MODE_CTRL
  {0x3238, 0x0444}, // EXPOSURE_RATIO

  {0x1008, 0x0361}, // FINE_INTEGRATION_TIME_MIN
  {0x100C, 0x0589}, // FINE_INTEGRATION_TIME2_MIN
  {0x100E, 0x07B1}, // FINE_INTEGRATION_TIME3_MIN
  {0x1010, 0x0139}, // FINE_INTEGRATION_TIME4_MIN

  // TODO: do these have to be lower than LINE_LENGTH_PCK?
  {0x3014, 0x08CB}, // FINE_INTEGRATION_TIME_
  {0x321E, 0x0894}, // FINE_INTEGRATION_TIME2

  {0x31D0, 0x0000}, // COMPANDING, no good in 10 bit?
  {0x33DA, 0x0000}, // COMPANDING
  {0x318E, 0x0200}, // PRE_HDR_GAIN_EN

  // DLO Settings
  {0x3100, 0x4000}, // DLO_CONTROL0
  {0x3280, 0x0CCC}, // T1 G1
  {0x3282, 0x0CCC}, // T1 R
  {0x3284, 0x0CCC}, // T1 B
  {0x3286, 0x0CCC}, // T1 G2
  {0x3288, 0x0FA0}, // T2 G1
  {0x328A, 0x0FA0}, // T2 R
  {0x328C, 0x0FA0}, // T2 B
  {0x328E, 0x0FA0}, // T2 G2

   // Initial Gains
  {0x3022, 0x0001}, // GROUPED_PARAMETER_HOLD_
  {0x3366, 0xFF77}, // ANALOG_GAIN (1x)

  {0x3060, 0x3333}, // ANALOG_COLOR_GAIN

  {0x3362, 0x0000}, // DC GAIN

  {0x305A, 0x00F8}, // red gain
  {0x3058, 0x0122}, // blue gain
  {0x3056, 0x009A}, // g1 gain
  {0x305C, 0x009A}, // g2 gain

  {0x3022, 0x0000}, // GROUPED_PARAMETER_HOLD_

  // Initial Integration Time
  {0x3012, 0x0005},
};
