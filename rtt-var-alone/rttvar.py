import math

import numpy as np
from matplotlib import pyplot as plt

fnames = {"rtt140--160.plot":("140 - 160 ms",'fig.text(0.7, 0.685, "140 - 160 ms", fontsize=20, rotation=-14, color="goldenrod")'),
          "rtt145--155.plot":("145 - 155 ms",'fig.text(0.7, 0.75, "145 - 155 ms", fontsize=20, rotation=-10, color=all_colors["145 - 155 ms"])'),
          "rtt50--250.plot":("50 - 250 ms",'fig.text(0.7, 0.8, "50 - 250 ms", fontsize=20, rotation=-5, color=all_colors["50 - 250 ms"])'),
          "rtt150.plot":("150 ms exactly",'fig.text(0.22, 0.62, "150 ms exactly", fontsize=20, rotation=68, color=all_colors["150 ms exactly"])'),
          "cubic.plot":("Cubic",'fig.text(0.4, 0.34, "Cubic", fontsize=20, rotation=0, color=all_colors["Cubic"])'),
          "cubicsfqCoDel.plot":("Cubic-over-sfqCoDel",'fig.text(0.45, 0.57, "Cubic-over-sfqCoDel", fontsize=20, rotation=-33, color=all_colors["Cubic-over-sfqCoDel"])')
          }

order=['Cubic', 'Cubic-over-sfqCoDel', '150 ms exactly', '145 - 155 ms', '140 - 160 ms', '50 - 250 ms']

all_data = {}
all_colors = {}
colors = plt.get_cmap('Dark2')(np.linspace(0, 1.0, 6))

for datafile, (name, command) in fnames.iteritems():
    with open(datafile, "rb") as f:
        all_data[name] = ([line.strip().split() for line in f.readlines()], command)

def normalize(x, y, idx):
    return math.log(y/(0.75 * 31.622)) - math.log(x/(2*idx))

fig = plt.figure()
plt.xlabel("RTT in ms")
plt.ylabel("Normalized objective function")
plt.xlim(0, 300)
plt.ylim(-2.0, 0.05)
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.labelpad = 16
ax.yaxis.labelpad = 16
plt.savefig("outfiles/rtt-base.pdf", bbox_inches="tight")
plt.plot([0, 500], [0, 0], linewidth=3, color="blue")
fig.text(0.75, 0.84, "Omniscient", fontsize=20, color="blue")
plt.savefig("outfiles/rtt-omniscient.pdf", bbox_inches="tight")

artists = []
for j, title in enumerate(order):
    data, linelabel = all_data[title]
    for a in artists:
        a.set_alpha(0.3)
    yvals = [normalize(float(d[2]), float(d[1]), i+1) for i, d in enumerate(data)]
    xvals = [float(d[0]) * 2 for d in data]
    color = colors[j]
    ar = plt.plot(xvals, yvals, label=title, color=color)
    artists.append(ar[0])
    all_colors[title] = color
    
    eval(linelabel)

    plt.savefig("outfiles/rtt-" + title.replace(' ', '-').replace('---', '-') + ".pdf", bbox_inches="tight")




