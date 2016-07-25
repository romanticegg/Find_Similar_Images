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


root1 = 'Dataset/'
root2 = 'Modified/'

for subdir, dirs, files in os.walk(root2):
	files.sort()
	for file in files:
		pa = str(root2) + str(file)
		img = cv2.imread(pa)
		print "Started for ",file
		x,y,z = img.shape
		check = 0
		if x in range(500,600) and y in range(850, 1100):
			img = cv2.resize(img,(960, 540), interpolation = cv2.INTER_CUBIC)
		elif (x>600) and (y>1100):
			img2 = img
			check = 1
		elif (x<500) and (y<850):
			img1 = img
			check = 2

		newimg = cv2.resize(img,(960, 540), interpolation = cv2.INTER_CUBIC)
		inhist = cv2.calcHist([newimg], [0, 1, 2], None, [64,64,64],
					[0, 256, 0, 256, 0, 256])
		inhist = cv2.normalize(inhist, inhist, 0,255, cv2.NORM_MINMAX).flatten()

		new_gray = cv2.cvtColor(newimg, cv2.COLOR_BGR2GRAY)
		ikhist = cv2.calcHist([new_gray],[0],None,[64],[0,256])
		ikhist = cv2.normalize(ikhist, ikhist, 0,255, cv2.NORM_MINMAX)

		ibhist = cv2.calcHist([newimg],[0],None,[64],[0,256])
		ibhist = cv2.normalize(ibhist, ibhist, 0,255, cv2.NORM_MINMAX)

		ighist = cv2.calcHist([newimg],[1],None,[64],[0,256])
		ighist = cv2.normalize(ighist, ighist, 0,255, cv2.NORM_MINMAX)

		irhist = cv2.calcHist([newimg],[2],None,[64],[0,256])
		irhist = cv2.normalize(irhist, irhist, 0,255, cv2.NORM_MINMAX)

		one,two = file.split('.')
		one = 'Analysis/analysis-' + one + '.csv'
		
		all = []
		all.append([one])
		all.append([''])
		all.append(['Files/Channels','Normal','GrayScale','Blue','Green','Red'])
		histo = []
		feature = []
		
		for subdir1, dirs1, files1 in os.walk(root1):
			files1.sort()
			for file1 in files1:
				print "Checking ",file1
				new = []

				pa1 = str(root1) + str(file1)
				image = cv2.imread(pa1)
				nhist = cv2.calcHist([image], [0, 1, 2], None, [64,64,64],
					[0, 256, 0, 256, 0, 256])
				nhist = cv2.normalize(nhist, nhist, 0,255, cv2.NORM_MINMAX).flatten()

				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				khist = cv2.calcHist([gray],[0],None,[64],[0,256])
				khist = cv2.normalize(khist, khist, 0,255, cv2.NORM_MINMAX)

				bhist = cv2.calcHist([image],[0],None,[64],[0,256])
				bhist = cv2.normalize(bhist, bhist, 0,255, cv2.NORM_MINMAX)

				ghist = cv2.calcHist([image],[1],None,[64],[0,256])
				ghist = cv2.normalize(ghist, ghist, 0,255, cv2.NORM_MINMAX)

				rhist = cv2.calcHist([image],[2],None,[64],[0,256])
				rhist = cv2.normalize(rhist, rhist, 0,255, cv2.NORM_MINMAX)

				d1 = cv2.compareHist(inhist, nhist, 0)
				d2 = cv2.compareHist(ikhist, khist, 0)
				d3 = cv2.compareHist(ibhist, bhist, 0)
				d4 = cv2.compareHist(ighist, ghist, 0)
				d5 = cv2.compareHist(irhist, rhist, 0)
				new.append(file1)
				new.append(d1)
				new.append(d2)
				new.append(d3)
				new.append(d4)
				new.append(d5)
				histo.append(new)
				print new
				new = []

				if(check==0):
					img1 = img
					img2 = cv2.imread(pa1)
				elif(check==1):
					img1 = cv2.imread(pa1)
				else:
					img2 = cv2.imread(pa1)
				
				# img2 = cv2.imread('Dataset/cofee-s1-00186.jpg',0) # trainImage

				# Initiate SIFT detector
				sift = cv2.xfeatures2d.SIFT_create()

				# find the keypoints and descriptors with SIFT
				kp1, des1 = sift.detectAndCompute(img1,None)
				kp2, des2 = sift.detectAndCompute(img2,None)

				c1 = len(kp1)
				c2 = len(kp2)
				# print c1, c2
				bf = cv2.BFMatcher()
				matches = bf.knnMatch(des1,des2, k=2)
				# print matches

				# Apply ratio test
				counter = 0
				mcounter=0
				good = []
				for m,n in matches:
				    if m.distance < 0.75*n.distance:
				        good.append([m])
				        counter+=1
					mcounter+=1

				# cv2.drawMatchesKnn expects list of lists as matches.
				img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
				#print file, " matches = ",counter
				gperc = counter/(c1*1.0)
				mperc = mcounter/(c1*1.0)
				new.append(file1)
				new.append(c1)
				new.append(counter)
				new.append(mcounter)
				new.append(gperc)
				new.append(mperc)
				feature.append(new)
				print new

		cw = open(one, 'w')
		rw = csv.writer(cw, lineterminator='\n')
		all = all + histo
		all.append([''])
		all.append(['FileName','Keypoints','Good Matches', 'All Matches', 'Good Perc', 'All Perc'])
		all = all + feature
		# print all
		rw.writerows(all)
		cw.close()
		print "############ Done for ",file, "###########"


	



