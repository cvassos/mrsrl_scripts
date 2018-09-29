import os
import re
import subprocess as sp
import csv

#Arrange the options we'd like to sweep over
win_lens = ['100K', '500K', '1M']
parallelargs = ['1','2','5']
Nruns = 4
outputs = []

filename = "sweepout.csv"
with open(filename,'wb') as myfile:
	wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
	
	for i in range(1,Nruns+1):
		for x in win_lens:
		    for y in parallelargs:
			#Run Iperf & Extract out the speeds from the tests
			if int(y) > 1:
				iperf = sp.Popen(('iperf','-c192.168.11.143','-t20',''.join(('-w',x)),''.join(('-P',y))),stdout=sp.PIPE)
				grep = sp.Popen(('grep','SUM'),stdin=iperf.stdout,stdout=sp.PIPE)
				iperf.stdout.close()
				outtext = grep.communicate()
			else:
				iperf = sp.Popen(('iperf','-c192.168.11.143','-t20',''.join(('-w',x)),''.join(('-P',y))),stdout=sp.PIPE)
				outtext = iperf.communicate()
			matches = re.findall("([0-9]*\.?[0-9])(?: Mbits/sec)",outtext[0])
			data = [x,y,matches[0]]
			wr.writerow(data)
			
			outputs.append(data)

