#!/usr/bin/python2.7
# coding: utf-8

import matplotlib.pyplot as plt
import re 
#import datetime

plotpoint=0
x=[]
y1=[]
y2=[]

with open('/Users/kathyly/desktop/bash_project/logs/2017-10-16.log','r') as f:
	for line in f:		
		tl = re.findall('\d+', line)
		#x.append(tl[4]+":"+tl[5]+":"+tl[6])
		x.append(plotpoint)
		y1.append(tl[0]+"."+tl[1])
		y2.append(tl[2]+"."+tl[3])
		#print tempentry
		if plotpoint > 24:
			break
		plotpoint=plotpoint+1

plt.subplot(2,1,1)
plt.plot(x,y1,'o-')
plt.title('CPU STATS')
plt.ylabel('CPU Usage (%)')
plt.xlabel("Time (Hour)")
plt.subplot(2,1,2)
plt.plot(x,y2,'o-')
plt.ylabel('Core Temp (C)')
plt.show()
plt.xlabel("Time (Hour)")

#DATA=$(date +%Y-%m-%d)
#cd users/kathyly/desktop/logs/$DATA.log
