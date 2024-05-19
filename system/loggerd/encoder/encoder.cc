#include "system/loggerd/encoder/encoder.h"

VideoEncoder::VideoEncoder(const EncoderInfo &encoder_info, int in_width, int in_height)
    : encoder_info(encoder_info), in_width(in_width), in_height(in_height) {

  out_width = encoder_info.frame_width > 0 ? encoder_info.frame_width : in_width;
  out_height = encoder_info.frame_height > 0 ? encoder_info.frame_height : in_height;

  std::vector pubs = {encoder_info.publish_name};
  if (encoder_info.thumbnail_name != NULL) {
    pubs.push_back(encoder_info.thumbnail_name);
  }
  pm.reset(new PubMaster(pubs));
}

void VideoEncoder::publisher_publish(VideoEncoder *e, int segment_num, uint32_t idx, VisionIpcBufExtra &extra,
                                     unsigned int flags, kj::ArrayPtr<capnp::byte> header, kj::ArrayPtr<capnp::byte> dat) {
  // broadcast packet
  MessageBuilder msg;
  auto event = msg.initEvent(true);
  auto edat = (event.*(e->encoder_info.init_encode_data_func))();
  auto edata = edat.initIdx();
  struct timespec ts;
  timespec_get(&ts, TIME_UTC);
  edat.setUnixTimestampNanos((uint64_t)ts.tv_sec*1000000000 + ts.tv_nsec);
  edata.setFrameId(extra.frame_id);
  edata.setTimestampSof(extra.timestamp_sof);
  edata.setTimestampEof(extra.timestamp_eof);
  edata.setType(e->encoder_info.encode_type);
  edata.setEncodeId(e->cnt++);
  edata.setSegmentNum(segment_num);
  edata.setSegmentId(idx);
  edata.setFlags(flags);
  edata.setLen(dat.size());
  edat.setData(dat);
  edat.setWidth(out_width);
  edat.setHeight(out_height);
  if (flags & V4L2_BUF_FLAG_KEYFRAME) edat.setHeader(header);

  uint32_t bytes_size = capnp::computeSerializedSizeInWords(msg) * sizeof(capnp::word);
  if (e->msg_cache.size() < bytes_size) {
    e->msg_cache.resize(bytes_size);
  }
  kj::ArrayOutputStream output_stream(kj::ArrayPtr<capnp::byte>(e->msg_cache.data(), bytes_size));
  capnp::writeMessage(output_stream, msg);
  e->pm->send(e->encoder_info.publish_name, e->msg_cache.data(), bytes_size);

  // Publish keyframe thumbnail
  if ((flags & V4L2_BUF_FLAG_KEYFRAME) && e->encoder_info.thumbnail_name != NULL && segment_num > last_thumbnail_segment) {
    last_thumbnail_segment = segment_num;

    MessageBuilder tm;
    auto thumbnail = tm.initEvent().initThumbnail();
    thumbnail.setFrameId(extra.frame_id);
    thumbnail.setTimestampEof(extra.timestamp_eof);
    thumbnail.setThumbnail(dat);
    thumbnail.setEncoding(cereal::Thumbnail::Encoding::KEYFRAME);
    pm->send(e->encoder_info.thumbnail_name, tm);
  }
}