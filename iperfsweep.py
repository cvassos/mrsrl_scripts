import os
import re
import subprocess
import csv

#Arrange the options we'd like to sweep over
win_lens = ['100K', '500K', '1M', '2M']
parallelargs = ['1','2','5','10']
outputs = []

for x in win_lens:
    for y in parallelargs:
        #Run Iperf & Extract out the speeds from the tests
        iperf = subprocess.Popen(('iperf','-c','-t20','-O10',''.join(('-w',x)),''.join(('-P',y))),stdout=subprocess.PIPE)
        iptext = iperf.communicate()
        matches = re.findall("([0-9]*\.[0-9])(?: Mbits/sec)",iptext)
        data = [x,y,gp]
        outputs.append(data)

print(outputs)
