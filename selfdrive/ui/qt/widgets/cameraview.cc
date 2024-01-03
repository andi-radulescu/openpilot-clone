#include "selfdrive/ui/qt/widgets/cameraview.h"

#ifdef __APPLE__
#include <OpenGL/gl3.h>
#else
#include <GLES3/gl3.h>
#endif

namespace {

const char frame_vertex_shader[] =
#ifdef __APPLE__
  "#version 330 core\n"
#else
  "#version 300 es\n"
#endif
  "layout(location = 0) in vec4 aPosition;\n"
  "layout(location = 1) in vec2 aTexCoord;\n"
  "uniform mat4 uTransform;\n"
  "out vec2 vTexCoord;\n"
  "void main() {\n"
  "  gl_Position = uTransform * aPosition;\n"
  "  vTexCoord = aTexCoord;\n"
  "}\n";

const char frame_fragment_shader[] =
#ifdef QCOM2
  "#version 300 es\n"
  "#extension GL_OES_EGL_image_external_essl3 : enable\n"
  "precision mediump float;\n"
  "uniform samplerExternalOES uTexture;\n"
  "in vec2 vTexCoord;\n"
  "out vec4 colorOut;\n"
  "void main() {\n"
  "  colorOut = texture(uTexture, vTexCoord);\n"
  "}\n";
#else
#ifdef __APPLE__
  "#version 330 core\n"
#else
  "#version 300 es\n"
  "precision mediump float;\n"
#endif
  "uniform sampler2D uTextureY;\n"
  "uniform sampler2D uTextureUV;\n"
  "in vec2 vTexCoord;\n"
  "out vec4 colorOut;\n"
  "void main() {\n"
  "  float y = texture(uTextureY, vTexCoord).r;\n"
  "  vec2 uv = texture(uTextureUV, vTexCoord).rg - 0.5;\n"
  "  float r = y + 1.402 * uv.y;\n"
  "  float g = y - 0.344 * uv.x - 0.714 * uv.y;\n"
  "  float b = y + 1.772 * uv.x;\n"
  "  colorOut = vec4(r, g, b, 1.0);\n"
  "}\n";
#endif

mat4 get_driver_view_transform(int screen_width, int screen_height, int stream_width, int stream_height) {
  const float driver_view_ratio = 2.0;
  const float yscale = stream_height * driver_view_ratio / stream_width;
  const float xscale = yscale*screen_height/screen_width*stream_width/stream_height;
  mat4 transform = (mat4){{
    xscale,  0.0, 0.0, 0.0,
    0.0,  yscale, 0.0, 0.0,
    0.0,  0.0, 1.0, 0.0,
    0.0,  0.0, 0.0, 1.0,
  }};
  return transform;
}

mat4 get_fit_view_transform(float widget_aspect_ratio, float frame_aspect_ratio) {
  float zx = 1, zy = 1;
  if (frame_aspect_ratio > widget_aspect_ratio) {
    zy = widget_aspect_ratio / frame_aspect_ratio;
  } else {
    zx = frame_aspect_ratio / widget_aspect_ratio;
  }

  const mat4 frame_transform = {{
    zx, 0.0, 0.0, 0.0,
    0.0, zy, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0,
  }};
  return frame_transform;
}

} // namespace

CameraWidget::CameraWidget(std::string stream_name, VisionStreamType type, bool zoom, QWidget *parent)
    : stream_name(stream_name), requested_stream_type(type), zoomed_view(zoom), QOpenGLWidget(parent) {
}

CameraWidget::~CameraWidget() {
  makeCurrent();
  if (isValid()) {
    glDeleteVertexArrays(1, &frame_vao);
    glDeleteBuffers(1, &frame_vbo);
    glDeleteBuffers(1, &frame_ibo);
    glDeleteBuffers(2, textures);
  }
#ifdef QCOM2
  EGLDisplay egl_display = eglGetCurrentDisplay();
  for (auto &pair : egl_images) {
    eglDestroyImageKHR(egl_display, pair.second);
  }
  egl_images.clear();
#endif
  doneCurrent();
}

// Qt uses device-independent pixels, depending on platform this may be
// different to what OpenGL uses
int CameraWidget::glWidth() {
    return width() * devicePixelRatio();
}

int CameraWidget::glHeight() {
  return height() * devicePixelRatio();
}

void CameraWidget::initializeGL() {
  initializeOpenGLFunctions();

  program = std::make_unique<QOpenGLShaderProgram>(context());
  bool ret = program->addShaderFromSourceCode(QOpenGLShader::Vertex, frame_vertex_shader);
  assert(ret);
  ret = program->addShaderFromSourceCode(QOpenGLShader::Fragment, frame_fragment_shader);
  assert(ret);

  program->link();
  GLint frame_pos_loc = program->attributeLocation("aPosition");
  GLint frame_texcoord_loc = program->attributeLocation("aTexCoord");

  auto [x1, x2, y1, y2] = requested_stream_type == VISION_STREAM_DRIVER ? std::tuple(0.f, 1.f, 1.f, 0.f) : std::tuple(1.f, 0.f, 1.f, 0.f);
  const uint8_t frame_indicies[] = {0, 1, 2, 0, 2, 3};
  const float frame_coords[4][4] = {
    {-1.0, -1.0, x2, y1}, // bl
    {-1.0,  1.0, x2, y2}, // tl
    { 1.0,  1.0, x1, y2}, // tr
    { 1.0, -1.0, x1, y1}, // br
  };

  glGenVertexArrays(1, &frame_vao);
  glBindVertexArray(frame_vao);
  glGenBuffers(1, &frame_vbo);
  glBindBuffer(GL_ARRAY_BUFFER, frame_vbo);
  glBufferData(GL_ARRAY_BUFFER, sizeof(frame_coords), frame_coords, GL_STATIC_DRAW);
  glEnableVertexAttribArray(frame_pos_loc);
  glVertexAttribPointer(frame_pos_loc, 2, GL_FLOAT, GL_FALSE,
                        sizeof(frame_coords[0]), (const void *)0);
  glEnableVertexAttribArray(frame_texcoord_loc);
  glVertexAttribPointer(frame_texcoord_loc, 2, GL_FLOAT, GL_FALSE,
                        sizeof(frame_coords[0]), (const void *)(sizeof(float) * 2));
  glGenBuffers(1, &frame_ibo);
  glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, frame_ibo);
  glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(frame_indicies), frame_indicies, GL_STATIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, 0);
  glBindVertexArray(0);

  glUseProgram(program->programId());

#ifdef QCOM2
  glUniform1i(program->uniformLocation("uTexture"), 0);
#else
  glGenTextures(2, textures);
  glUniform1i(program->uniformLocation("uTextureY"), 0);
  glUniform1i(program->uniformLocation("uTextureUV"), 1);
#endif
}

void CameraWidget::updateFrameMat() {
  int w = glWidth(), h = glHeight();

  if (zoomed_view) {
    if (streamType() == VISION_STREAM_DRIVER) {
      if (stream_width > 0 && stream_height > 0) {
        frame_mat = get_driver_view_transform(w, h, stream_width, stream_height);
      }
    } else {
      // Project point at "infinity" to compute x and y offsets
      // to ensure this ends up in the middle of the screen
      // for narrow come and a little lower for wide cam.
      // TODO: use proper perspective transform?
      if (streamType() == VISION_STREAM_WIDE_ROAD) {
        intrinsic_matrix = ECAM_INTRINSIC_MATRIX;
        zoom = 2.0;
      } else {
        intrinsic_matrix = FCAM_INTRINSIC_MATRIX;
        zoom = 1.1;
      }
      const vec3 inf = {{1000., 0., 0.}};
      const vec3 Ep = matvecmul3(calibration, inf);
      const vec3 Kep = matvecmul3(intrinsic_matrix, Ep);

      float x_offset_ = (Kep.v[0] / Kep.v[2] - intrinsic_matrix.v[2]) * zoom;
      float y_offset_ = (Kep.v[1] / Kep.v[2] - intrinsic_matrix.v[5]) * zoom;

      float max_x_offset = intrinsic_matrix.v[2] * zoom - w / 2 - 5;
      float max_y_offset = intrinsic_matrix.v[5] * zoom - h / 2 - 5;

      x_offset = std::clamp(x_offset_, -max_x_offset, max_x_offset);
      y_offset = std::clamp(y_offset_, -max_y_offset, max_y_offset);

      float zx = zoom * 2 * intrinsic_matrix.v[2] / w;
      float zy = zoom * 2 * intrinsic_matrix.v[5] / h;
      const mat4 frame_transform = {{
        zx, 0.0, 0.0, -x_offset / w * 2,
        0.0, zy, 0.0, y_offset / h * 2,
        0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0,
      }};
      frame_mat = frame_transform;
    }
  } else if (stream_width > 0 && stream_height > 0) {
    // fit frame to widget size
    float widget_aspect_ratio = (float)w / h;
    float frame_aspect_ratio = (float)stream_width  / stream_height;
    frame_mat = get_fit_view_transform(widget_aspect_ratio, frame_aspect_ratio);
  }
}

void CameraWidget::updateCalibration(const mat3 &calib) {
  calibration = calib;
}

void CameraWidget::paintGL() {
  glClearColor(bg.redF(), bg.greenF(), bg.blueF(), bg.alphaF());
  glClear(GL_STENCIL_BUFFER_BIT | GL_COLOR_BUFFER_BIT);

  if (!frame) return;

  // Log duplicate/dropped frames
  if (frame_id == prev_frame_id) {
    qDebug() << "Drawing same frame twice" << frame_id;
  } else if (frame_id != prev_frame_id + 1) {
    qDebug() << "Skipped frame" << frame_id;
  }
  prev_frame_id = frame_id;

  updateFrameMat();

  glViewport(0, 0, glWidth(), glHeight());
  glBindVertexArray(frame_vao);
  glUseProgram(program->programId());
  glPixelStorei(GL_UNPACK_ALIGNMENT, 1);

#ifdef QCOM2
  // no frame copy
  glActiveTexture(GL_TEXTURE0);
  glEGLImageTargetTexture2DOES(GL_TEXTURE_EXTERNAL_OES, egl_images[frame->idx]);
  assert(glGetError() == GL_NO_ERROR);
#else
  // fallback to copy
  glPixelStorei(GL_UNPACK_ROW_LENGTH, stream_stride);
  glActiveTexture(GL_TEXTURE0);
  glBindTexture(GL_TEXTURE_2D, textures[0]);
  glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, stream_width, stream_height, GL_RED, GL_UNSIGNED_BYTE, frame->y);
  assert(glGetError() == GL_NO_ERROR);

  glPixelStorei(GL_UNPACK_ROW_LENGTH, stream_stride/2);
  glActiveTexture(GL_TEXTURE0 + 1);
  glBindTexture(GL_TEXTURE_2D, textures[1]);
  glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, stream_width/2, stream_height/2, GL_RG, GL_UNSIGNED_BYTE, frame->uv);
  assert(glGetError() == GL_NO_ERROR);
#endif

  glUniformMatrix4fv(program->uniformLocation("uTransform"), 1, GL_TRUE, frame_mat.v);
  glEnableVertexAttribArray(0);
  glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_BYTE, (const void *)0);
  glDisableVertexAttribArray(0);
  glBindVertexArray(0);
  glBindTexture(GL_TEXTURE_2D, 0);
  glActiveTexture(GL_TEXTURE0);
  glPixelStorei(GL_UNPACK_ALIGNMENT, 4);
  glPixelStorei(GL_UNPACK_ROW_LENGTH, 0);
}

void CameraWidget::vipcConnected() {
  makeCurrent();
  stream_width = vipc_client->buffers[0].width;
  stream_height = vipc_client->buffers[0].height;
  stream_stride = vipc_client->buffers[0].stride;

#ifdef QCOM2
  EGLDisplay egl_display = eglGetCurrentDisplay();
  assert(egl_display != EGL_NO_DISPLAY);
  for (auto &pair : egl_images) {
    eglDestroyImageKHR(egl_display, pair.second);
  }
  egl_images.clear();

  for (int i = 0; i < vipc_client->num_buffers; i++) {  // import buffers into OpenGL
    int fd = dup(vipc_client->buffers[i].fd);  // eglDestroyImageKHR will close, so duplicate
    EGLint img_attrs[] = {
      EGL_WIDTH, (int)vipc_client->buffers[i].width,
      EGL_HEIGHT, (int)vipc_client->buffers[i].height,
      EGL_LINUX_DRM_FOURCC_EXT, DRM_FORMAT_NV12,
      EGL_DMA_BUF_PLANE0_FD_EXT, fd,
      EGL_DMA_BUF_PLANE0_OFFSET_EXT, 0,
      EGL_DMA_BUF_PLANE0_PITCH_EXT, (int)vipc_client->buffers[i].stride,
      EGL_DMA_BUF_PLANE1_FD_EXT, fd,
      EGL_DMA_BUF_PLANE1_OFFSET_EXT, (int)vipc_client->buffers[i].uv_offset,
      EGL_DMA_BUF_PLANE1_PITCH_EXT, (int)vipc_client->buffers[i].stride,
      EGL_NONE
    };
    egl_images[i] = eglCreateImageKHR(egl_display, EGL_NO_CONTEXT, EGL_LINUX_DMA_BUF_EXT, 0, img_attrs);
    assert(eglGetError() == EGL_SUCCESS);
  }
#else
  glBindTexture(GL_TEXTURE_2D, textures[0]);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
  glTexImage2D(GL_TEXTURE_2D, 0, GL_R8, stream_width, stream_height, 0, GL_RED, GL_UNSIGNED_BYTE, nullptr);
  assert(glGetError() == GL_NO_ERROR);

  glBindTexture(GL_TEXTURE_2D, textures[1]);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
  glTexImage2D(GL_TEXTURE_2D, 0, GL_RG8, stream_width/2, stream_height/2, 0, GL_RG, GL_UNSIGNED_BYTE, nullptr);
  assert(glGetError() == GL_NO_ERROR);
#endif
}

bool CameraWidget::receiveFrame(uint64_t request_frame_id) {
  if (!vipc_client || vipc_client->type != requested_stream_type) {
    qDebug().nospace() << "connecting to stream" << requested_stream_type
                       << (vipc_client ? QString(", was connected to %1").arg(vipc_client->type) : "");
    vipc_client.reset(new VisionIpcClient(stream_name, requested_stream_type, false));
  }

  if (!vipc_client->connected) {
    frame = nullptr;
    recent_frames.clear();
    available_streams = VisionIpcClient::getAvailableStreams(stream_name, false);
    if (available_streams.empty() || !vipc_client->connect(false)) {
      return false;
    }
    emit vipcAvailableStreamsUpdated();
    vipcConnected();
  }

  VisionIpcBufExtra meta_main = {};
  while (auto buf = vipc_client->recv(&meta_main, 0)) {
    if (recent_frames.size() > FRAME_BUFFER_SIZE) {
      recent_frames.pop_front();
    }
    recent_frames.emplace_back(meta_main.frame_id, buf);
  }

  frame = nullptr;
  if (request_frame_id > 0) {
    auto it = std::find_if(recent_frames.begin(), recent_frames.end(),
                           [request_frame_id](auto &f) { return f.first == request_frame_id; });
    if (it != recent_frames.end()) {
      std::tie(frame_id, frame) = *it;
    }
  } else if (!recent_frames.empty()) {
    std::tie(frame_id, frame) = recent_frames.back();
  }
  return frame != nullptr;
}

void CameraWidget::disconnectVipc() {
  recent_frames.clear();
  frame = nullptr;
  frame_id = 0;
  prev_frame_id = 0;
  if (vipc_client) {
    vipc_client->connected = false;
  }
}

// Cameraview

CameraView::CameraView(const std::string &name, VisionStreamType stream_type, bool zoom, QWidget *parent)
    : CameraWidget(name, stream_type, zoom, parent) {
  timer = new QTimer(this);
  timer->setInterval(1000.0 / UI_FREQ);
  timer->callOnTimeout(this, [this]() { if (receiveFrame()) update(); });
}

void CameraView::showEvent(QShowEvent *event) {
  timer->start();
}

void CameraView::hideEvent(QHideEvent *event) {
  timer->stop();
  disconnectVipc();
}
