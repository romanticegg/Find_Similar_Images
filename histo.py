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


root = 'Dataset/'
d = set()
green = {}
blue = {}
red = {}
black = {}
normal = {}
main = {}
counter = 1
for subdir, dirs, files in os.walk(root):
	files.sort()
	# print files
	for file in files:
		pa = str(root) + str(file)
		img = cv2.imread(pa)
		main[file] = counter
		counter+=1
		# print file
		gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		blhist = cv2.calcHist([gray_image],[0],None,[64],[0,256])
		blhist = cv2.normalize(blhist, blhist, 0,255, cv2.NORM_MINMAX)
		plt.plot(blhist,color = 'k')
		plt.xlim([0,70])
		black[file] = blhist
		color = ('b','g','r')
		hist = cv2.calcHist([img], [0, 1, 2], None, [64,64,64],
			[0, 256, 0, 256, 0, 256])
		hist = cv2.normalize(hist, blhist, 0,255, cv2.NORM_MINMAX).flatten()
		# print hist
		# normal[file] = hist
		for i,col in enumerate(color):
			histr = cv2.calcHist([img],[i],None,[64],[0,256])
			# histr = cv2.normalize(histr)
			plt.plot(histr,color = col)
			plt.xlim([0,70])
			if i==0:
				blue[file] = histr
			elif i==1:
				green[file] = histr
			else:
				red[file] = histr

		# plt.title(file)
		# plt.show()

methods = ('CV_COMP_CORREL', 'CV_COMP_CHISQR', 'CV_COMP_INTERSECT', 'CV_COMP_BHATTACHARYYA')
# methods1 = (dist.euclidean, dist.cityblock, dist.chebyshev) // useless hain ye
allg = [[]]
allb = [[]]
allr = [[]]
allk = [[]]

main1 = OrderedDict(sorted(main.items(), key=itemgetter(1)))

template = []
l = []
l.append('Name of image')
for key, value in main1.iteritems():
	l.append(key)
template.append(l)
c = 1
li = []
for key, value in main1.iteritems():
	li.append('')
for key, value in main1.iteritems():
	print c
	lis = []
	lis.append(key)
	template.append(lis)
	template[c] = template[c] + li
	c+=1

for i in xrange(4):
	c = open('black.csv', 'r')
	all = []
	data = csv.reader(c)
	all = list(data)
	all.append([])
	all.append([methods[i]])
	new = template
	for key, value in black.iteritems():
		p = main[key]
		for key1, value1 in black.iteritems():
			d1 = cv2.compareHist(value, value1, i)
			q = main[key1]
			new[p][q] = d1
	c.close()

	all = all + new
	cw = open('black.csv', 'w')
	rw = csv.writer(cw, lineterminator='\n')
	rw.writerows(all)
	cw.close()



	c = open('blue.csv', 'r')
	all = []
	data = csv.reader(c)
	all = list(data)
	all.append([])
	all.append([methods[i]])
	new = template
	for key, value in blue.iteritems():
		p = main[key]
		for key1, value1 in blue.iteritems():
			d1 = cv2.compareHist(value, value1, i)
			q = main[key1]
			new[p][q] = d1
	c.close()

	all = all + new
	cw = open('blue.csv', 'w')
	rw = csv.writer(cw, lineterminator='\n')
	rw.writerows(all)
	cw.close()

	c = open('green.csv', 'r')
	all = []
	data = csv.reader(c)
	all = list(data)
	all.append([])
	all.append([methods[i]])
	new = template
	for key, value in green.iteritems():
		p = main[key]
		for key1, value1 in green.iteritems():
			d1 = cv2.compareHist(value, value1, i)
			q = main[key1]
			new[p][q] = d1
	c.close()

	all = all + new
	cw = open('green.csv', 'w')
	rw = csv.writer(cw, lineterminator='\n')
	rw.writerows(all)
	cw.close()

	c = open('red.csv', 'r')
	all = []
	data = csv.reader(c)
	all = list(data)
	all.append([])
	all.append([methods[i]])
	new = template
	for key, value in red.iteritems():
		p = main[key]
		for key1, value1 in red.iteritems():
			d1 = cv2.compareHist(value, value1, i)
			q = main[key1]
			new[p][q] = d1
	c.close()

	all = all + new
	cw = open('red.csv', 'w')
	rw = csv.writer(cw, lineterminator='\n')
	rw.writerows(all)
	cw.close()

	c = open('normal.csv', 'r')
	all = []
	data = csv.reader(c)
	all = list(data)
	all.append([])
	all.append([methods[i]])
	new = template
	for key, value in normal.iteritems():
		p = main[key]
		for key1, value1 in normal.iteritems():
			d1 = cv2.compareHist(value, value1, i)
			q = main[key1]
			new[p][q] = d1
	c.close()

	all = all + new
	cw = open('normal.csv', 'w')
	rw = csv.writer(cw, lineterminator='\n')
	rw.writerows(all)
	cw.close()
			
