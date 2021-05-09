#pragma once

#include <fstream>
#include <string>

#include "cereal/gen/cpp/log.capnp.h"
#include "selfdrive/sensord/sensors/sensor.h"

class FileSensor : public Sensor {
protected:
  std::ifstream file;

public:
  FileSensor(std::string filename);
  ~FileSensor();
  int init();
  virtual void get_event(cereal::SensorEventData::Builder &event) = 0;
};
