#! /usr/bin/python
from scipy.misc import comb
import sys

link_speed = float(sys.argv[1])
min_rtt = float(sys.argv[2])

def compute_fair_share(muxing):
  # look at other senders from 0 to muxing - 1
  fair_share_sum = 0.0
  for senders in range(0, muxing):
    prob = comb(muxing - 1, senders, exact=True) * (0.5 ** (muxing - 1))
    fair_share_sum += prob / (1.0 + senders)
  return fair_share_sum

for i in range(1, 101):
  fshare = link_speed * compute_fair_share(i)
  print i, fshare, min_rtt
