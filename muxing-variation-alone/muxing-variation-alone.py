import math
import numpy as np
import re

from matplotlib import pyplot as plt

ylims = [-1.5, -5]
titles = ["Buffer size 5x BDP", "No packet drops"]
fnames = {"num_senders1--100.plot":("Tao 1 - 100",'fig.text(.8, 0.79, "1 - 100", fontsize=20, rotation=-2, color="purple")'),
          "num_senders1--2.plot":("Tao 1 - 2",'fig.text(0.18, 0.40, "1 - 2", fontsize=20, rotation=-87, color="red")'),
          "num_senderscubicsfqCoDel.plot":("Cubic-over-sfqCoDel",'fig.text(0.65, 0.67, "Cubic-over-sfqCoDel", fontsize=20, rotation=-8, color="#008080")'),
          "num_senders1--10.plot":("Tao 1 - 10",'fig.text(0.28, 0.30, "1 - 10", fontsize=20, rotation=-86, color="green")'),
          "num_senders1--50.plot":("Tao 1 - 50",'fig.text(0.55, 0.73, "1 - 50", fontsize=20, rotation=-20, color="brown")'),
          "num_senders1--20.plot":("Tao 1 - 20",'fig.text(0.43, 0.31, "1 - 20", fontsize=20, rotation=-67, color="blue")'),
          "num_senderscubic.plot":("Cubic",'fig.text(0.55, 0.56, "Cubic", fontsize=20, rotation=5, color="#ff9900")')
          }

order=['Tao 1 - 2', 'Tao 1 - 10', 'Tao 1 - 20', 'Tao 1 - 50', 'Tao 1 - 100', 'Cubic', 'Cubic-over-sfqCoDel']
colors = plt.get_cmap('Paired')(np.linspace(0, 1.0, 7))

fig = plt.figure()
artists = []
all_colors = {}
all_data = {}

for datafile, (name, command) in fnames.iteritems():
    with open("plots-5BDP-normalized/" + datafile, "rb") as f:
        all_data[name] = ([line.strip().split() for line in f.readlines()], command)

ax = fig.add_subplot(1, 1, 1)
ax.xaxis.labelpad = 16
ax.yaxis.labelpad = 16
plt.xlabel("Number of senders")
plt.ylabel("Normalized objective function")
plt.xlim(0, 100)
plt.ylim(-1.5, 1.5*0.05)
plt.savefig("outfiles/muxing-base.pdf", bbox_inches="tight")
ax.plot([0, 100], [0, 0], linewidth=3, color="black")
fig.text(0.25, 0.87, "Omniscient", fontsize=20, color="black")
plt.savefig("outfiles/muxing-omniscient.pdf", bbox_inches="tight")

def normalize(x, y):
    return math.log(y) - math.log(x)

for j, title in enumerate(order):
    data, linelabel = all_data[title]
    for a in artists:
        a.set_alpha(0.3)
    yvals = [normalize(float(d[2]), float(d[1])) for d in data]
    xvals = [float(d[0]) for d in data]
    col = re.search('color="(.*?)"', linelabel).group(1)
    vspanar = None
    if 'Tao' in title:
        num = int(title[8:])
        vspanar = plt.axvspan(0, num, alpha=0.2, color=col)
        plt.savefig("outfiles/muxing-span-" + title.replace(' ', '-').replace('---', '-') + ".pdf", bbox_inches="tight")
    all_colors[title] = col
    ar, = ax.plot(xvals, yvals, color=col, lw=3, label=title, alpha=1.0)
    artists.append(ar)

    eval(linelabel)

    plt.savefig("outfiles/muxing-" + title.replace(' ', '-').replace('---', '-') + ".pdf", bbox_inches="tight")
    if vspanar:
        vspanar.remove()
