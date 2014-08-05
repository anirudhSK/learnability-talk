set term png
set macros
formatting = "lw 4 w linespoints"

set style data lines

set yrange [*:*] noreverse
set output "muxing-agility-util.png"
set title  ""
set xlabel "Number of senders"
set ylabel "Normalized Objective Function"
!python compute_omniscient.py 15 150 > omniscient.plot
ordinate ="log ($2) - log ($3)"
set xrange [0:100]
set key font ",10"
set key outside horizontal
plot "<python normalize_to_omni.py plots-5BDP/num_senders1--2.plot           omniscient.plot" u 1:(@ordinate) @formatting t "Tao-1--2", \
     "<python normalize_to_omni.py plots-5BDP/num_senders1--10.plot          omniscient.plot" u 1:(@ordinate) @formatting t "Tao-1--10", \
     "<python normalize_to_omni.py plots-5BDP/num_senders1--20.plot          omniscient.plot" u 1:(@ordinate) @formatting t "Tao-1--20", \
     "<python normalize_to_omni.py plots-5BDP/num_senders1--50.plot          omniscient.plot" u 1:(@ordinate) @formatting t "Tao-1--50", \
     "<python normalize_to_omni.py plots-5BDP/num_senders1--100.plot         omniscient.plot" u 1:(@ordinate) @formatting t "Tao-1--100", \
     "<python normalize_to_omni.py plots-5BDP/num_senderscubic.plot          omniscient.plot" u 1:(@ordinate) @formatting t "cubic", \
     "<python normalize_to_omni.py plots-5BDP/num_senderscubicsfqCoDel.plot  omniscient.plot" u 1:(@ordinate) @formatting t "cubic-sfqCoDel", \
     0 lw 4 w lines t "omniscient"
