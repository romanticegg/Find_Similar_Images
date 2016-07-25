import json
import matplotlib.pyplot as plt
import numpy as np
import Tkinter
import sys
from operator import itemgetter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
import math
import cv2
import os
import time
import csv
from scipy.spatial import distance
from collections import OrderedDict
from operator import itemgetter
import random

root1 = 'Analysis/'

all = []
for subdir, dirs, files in os.walk(root1):
	files.sort()
	for file in files:
		pa = str(root1) + str(file)
		c = open(pa,'r')
		data = csv.reader(c)
		datal = list(data)
		row_count = len(datal)
		c.seek(0)
		num_files = (row_count - 5)/2
		hsame = {}
		hvery_sim = {}
		hless_sim = {}
		fsame = {}
		fvery_sim = {}
		fless_sim = {}
		it = num_files + 2
		for i in range(3,num_files+3):
			# print i
			val = float(datal[i][1])
			valf = float(datal[it+i][4])

			if (val>=0.95) and (val<=1):
				hsame[datal[i][0]] = datal[i][1]
				if (valf>=0.09):
					fsame[datal[it+i][0]] = float(datal[it+i][4])

			elif (val>=0.70) and (val<=0.95):
				hvery_sim[datal[i][0]] = datal[i][1]
				if (valf>=0.06):
					fvery_sim[datal[it+i][0]] = float(datal[it+i][4])

			elif (val>=0.52) and (val<=0.70):
				hless_sim[datal[i][0]] = datal[i][1]
				if (valf>=0.05):
					fless_sim[datal[it+i][0]] = float(datal[it+i][4])

		for i in range(it+3, it+3+num_files):
			valf = float(datal[i][4])
			na = datal[i][0]
			if (na not in fsame) and (na not in fvery_sim) and (na not in fless_sim):
				if (valf>=0.08) and (val<=0.20):
					fless_sim[na] = valf
				elif (valf>=0.2):
					fvery_sim[na] = valf

		main1 = OrderedDict(sorted(fsame.items(), key=itemgetter(1), reverse=True))
		main2 = OrderedDict(sorted(fvery_sim.items(), key=itemgetter(1), reverse=True))
		main3 = OrderedDict(sorted(fless_sim.items(), key=itemgetter(1), reverse=True))

		all.append([file])
		arr = ['Almost Same']
		for key,values in main1.iteritems():
			arr.append(key)
		all.append(arr)

		arr = ['Very Smiliar']
		for key,values in main2.iteritems():
			arr.append(key)
		all.append(arr)
		
		arr = ['Somewhat Smiliar']
		for key,values in main3.iteritems():
			arr.append(key)
		all.append(arr)
		all.append([''])

		print "#######Done for", file, "##############"
		print 

cw = open('Final_Report.csv', 'w')
rw = csv.writer(cw, lineterminator='\n')
rw.writerows(all)
cw.close()
print "---------------------Finally done-----------------"
			




