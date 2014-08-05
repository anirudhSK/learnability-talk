#! /usr/bin/python
import sys
data = sys.argv[1]
omniscient = sys.argv[2]

def parse_data(file_name):
  kv_store = dict()
  fh = open(file_name, "r");
  for line in fh.readlines():
    records = line.split()
    senders = int(records[0])
    tpt = float(records[1])
    delay = float(records[2])
    kv_store[senders] = (tpt, delay)
  return kv_store

data_kv = parse_data(data);
omni_kv = parse_data(omniscient);

for entry in data_kv:
  print entry, data_kv[entry][0]/omni_kv[entry][0], data_kv[entry][1]/omni_kv[entry][1]
