set term png
set macros
formatting = "lw 4 w lines"
set key bottom right

set style data lines

set yrange [*:*] noreverse
set output "rtt-agility-util.png"
set title  ""
set xlabel "RTT in ms"
set ylabel "Normalized objective function"
ordinate = "log ($2/(0.75 * 31.622)) - log($3/(2 * $1))"
plot "rtt10--280.plot" u (2 * $1):(@ordinate)  @formatting t "rtt10--280", \
     "rtt50--250.plot" u (2 * $1):(@ordinate)  @formatting t "rtt50--250", \
     "rtt110--200.plot" u (2 * $1):(@ordinate) @formatting t "rtt110--200", \
     "rtt140--160.plot" u (2 * $1):(@ordinate) @formatting t "rtt140--160", \
     "rtt145--155.plot" u (2 * $1):(@ordinate) @formatting t "rtt145--155", \
     "rtt150.plot" u (2 * $1):(@ordinate)      @formatting t "rtt150", \
     "cubic.plot" u (2 * $1):(@ordinate)       @formatting t "cubic", \
     "cubicsfqCoDel.plot" u (2 * $1):(@ordinate) @formatting t "cubicsfqCoDel", \
     0 lw 4 w lines t "omniscient"
