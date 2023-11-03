#pragma once

#include <QPixmap>
#include <QPointF>
#include <vector>

#include "tools/cabana/dbc/dbc.h"

class Sparkline {
public:
  void update(const MessageId &msg_id, const cabana::Signal *sig, double last_msg_ts, int range, QSize size);
  inline double freq() const { return freq_; }
  bool isEmpty() const { return pixmap.isNull(); }

  QPixmap pixmap;
  double min_val = 0;
  double max_val = 0;

private:
  void render(const QColor &color, int range, QSize size);

  std::vector<QPointF> points;
  double freq_ = 0;
};
