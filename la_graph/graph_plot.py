import os
import subprocess
import matplotlib.pyplot as p
import matplotlib as m
from datetime import datetime


count_columns = 0
onemin, fivemin, fifmin, bar_c = [], [], [], []

# subprocess.call(['bash', './info.sh'])

filename = open("/home/kali/Desktop/scr/info", "r")

while True:
    count_columns += 1

    bar_c.append(count_columns)
    line = filename.readline()
    if not line:
        break
    else:
        numbers = [float(x) for x in line.split()]
        x1, x2, x3 = numbers[0], numbers[1], numbers[2]
        onemin.append(x1)
        fivemin.append(x2)
        fifmin.append(x3)

bar_c.pop()
f = p.figure()
f.set_figheight(5)
f.set_figwidth(7)
f.set(facecolor = 'oldlace')
p.plot(bar_c, onemin, color = 'rosybrown', label = '1 min')
p.plot(bar_c, fivemin, color = 'olive', label = '5 min')
p.plot(bar_c, fifmin, color = 'slategrey', label = '15 min')
p.legend()
p.title('Load Average')
p.show()

