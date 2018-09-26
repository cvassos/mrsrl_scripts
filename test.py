import os
import re

filename = "iperf_ex"
infile = open(filename,'r')
filetext = infile.read()
infile.close()
matches = re.findall("([0-9]*\.[0-9])(?: Mbits/sec)",filetext)
print(matches)
vals = [float(i) for i in matches]
avg = vals[-1]

