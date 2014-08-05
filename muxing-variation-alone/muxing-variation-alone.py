import math
import numpy as np

from matplotlib import pyplot as plt

dirnames = ["plots-5BDP"]
norm_dirnames = ["plots-5BDP-normalized"]
ylims = [-1.5, -5]
titles = ["Buffer size 5x BDP", "No packet drops"]
fnames = {"num_senders1--100.plot":"Tao 1 - 100",
          "num_senders1--2.plot":"Tao 1 - 2",
          "num_senderscubicsfqCoDel.plot":"Cubic-over-sfqCoDel",
          "num_senders1--10.plot":"Tao 1 - 10",
          "num_senders1--50.plot":"Tao 1 - 50",
          "num_senders1--20.plot":"Tao 1 - 20",
          "num_senderscubic.plot":"Cubic"
          }


fig = plt.figure(figsize=(25, 8))
artists = []
all_colors = {}
for i in range(len(dirnames)):
    all_data = {}

    for datafile, name in fnames.iteritems():
        with open(norm_dirnames[i] + "/" + datafile, "rb") as f:
            all_data[name] = [line.strip().split() for line in f.readlines()]
 
    ax = fig.add_subplot(1, 2, i+1)
    ax.xaxis.labelpad = 16
    ax.yaxis.labelpad = 16
    #ax.set_xscale('log')

    def normalize(x, y):
        return math.log(y) - math.log(x)

    it = iter(sorted(all_data.iteritems()))
    colors = plt.get_cmap('Paired')(np.linspace(0, 1.0, 7))
    for j, (title, data) in enumerate(it):
        alpha = 1.0
        yvals = [normalize(float(d[2]), float(d[1])) for d in data]
        xvals = [float(d[0]) for d in data]
        ar, = ax.plot(xvals, yvals, color=colors[j], alpha=alpha, lw=3)
        all_colors[title] = colors[j]
        if i == 0:
            artists.append((ar, title))

    ax.plot([0, 100], [0, 0], linewidth=3)

    plt.xlabel("Number of senders")
    plt.ylabel("Normalized objective function")
    plt.xlim(0, 100)
    plt.ylim(ylims[i], -1*ylims[i]*0.05)
    plt.title(titles[i])

fig.text(0.8/2, 0.79, "1 - 100", fontsize=20, rotation=-2, color=all_colors["Tao 1 - 100"])
fig.text(0.305, 0.745, "1 - 50", fontsize=20, rotation=-20, color=all_colors["Tao 1 - 50"])
fig.text(0.37, 0.68, "Cubic-over-sfqCoDel", fontsize=20, rotation=-8, color=all_colors["Cubic-over-sfqCoDel"])
fig.text(0.26, 0.54, "Cubic", fontsize=20, rotation=5, color=all_colors["Cubic"])
fig.text(0.265, 0.31, "1 - 20", fontsize=20, rotation=-67, color=all_colors["Tao 1 - 20"])
fig.text(0.198, 0.30, "1 - 10", fontsize=20, rotation=-86, color=all_colors["Tao 1 - 10"])
fig.text(0.153, 0.40, "1 - 2", fontsize=20, rotation=-87, color=all_colors["Tao 1 - 2"])

fig.text(0.25, 0.87, "Omniscient", fontsize=20, color="blue")

plt.savefig("muxing-agility-util.pdf", bbox_inches="tight")
