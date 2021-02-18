#!/usr/bin/env python3
import os
import sys
import multiprocessing
import subprocess
import argparse
from tempfile import NamedTemporaryFile

from common.basedir import BASEDIR
from selfdrive.test.process_replay.compare_logs import save_log
from tools.lib.route import Route
from tools.lib.logreader import LogReader


def load_segment(segment_name):
  print(f"Loading {segment_name}")
  lr = LogReader(segment_name)
  r = [d for d in lr if d.which() not in ['can', 'sendcan']]
  print(f"done {segment_name}")
  return r

def juggle_file(fn):
  env = os.environ.copy()
  env["BASEDIR"] = BASEDIR
  juggle_dir = os.path.dirname(os.path.realpath(__file__))
  subprocess.call(f"bin/plotjuggler -d {fn}", shell=True, env=env, cwd=juggle_dir)

def juggle_route(route_name, segment_number):
  r = Route(route_name)

  logs = r.log_paths()
  if segment_number is not None:
    logs = logs[segment_number:segment_number+1]

  if None in logs:
    fallback_answer = input("At least one of the rlogs in this segment does not exist, would you like to use the qlogs? (y/n) : ")
    if fallback_answer == 'y':
      logs = r.qlog_paths()
      if segment_number is not None:
        logs = logs[segment_number:segment_number+1]
    else:
      print(f"Please try a different {'segment' if segment_number is not None else 'route'}")
      return

  all_data = []
  pool = multiprocessing.Pool(24)
  for d in pool.map(load_segment, logs):
    all_data += d

  tempfile = NamedTemporaryFile(suffix='.rlog')
  save_log(tempfile.name, all_data, compress=False)
  del all_data

  juggle_file(tempfile.name)

def get_arg_parser():
  parser = argparse.ArgumentParser(description="PlotJuggler plugin for reading rlogs",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  parser.add_argument("route_name", nargs='?', help="The name of the route that will be plotted.")
  parser.add_argument("segment_number", type=int, nargs='?', help="The index of the segment that will be plotted")
  return parser

if __name__ == "__main__":

  arg_parser = get_arg_parser()
  if len(sys.argv) == 1:
    arg_parser.print_help()
    sys.exit()
  args = arg_parser.parse_args(sys.argv[1:])
  juggle_route(args.route_name, args.segment_number)
