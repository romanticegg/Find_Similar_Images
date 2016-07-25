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


name = raw_input("Enter complete path of image: ")

img = cv2.imread(name)
# print "Started for ",file
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

root1 = 'Dataset/'

for subdir1, dirs1, files1 in os.walk(root1):
	files1.sort()
	for file1 in files1:
		print
		pa1 = str(root1) + str(file1)
		image = cv2.imread(pa1)
		nhist = cv2.calcHist([image], [0, 1, 2], None, [64,64,64],
			[0, 256, 0, 256, 0, 256])
		nhist = cv2.normalize(nhist, nhist, 0,255, cv2.NORM_MINMAX).flatten()

		val = cv2.compareHist(inhist, nhist, 0)

		if(check==0):
			img1 = img
			img2 = cv2.imread(pa1)
		elif(check==1):
			img1 = cv2.imread(pa1)
		else:
			img2 = cv2.imread(pa1)
		

		sift = cv2.xfeatures2d.SIFT_create()

		kp1, des1 = sift.detectAndCompute(img1,None)
		kp2, des2 = sift.detectAndCompute(img2,None)

		c1 = len(kp1)
		c2 = len(kp2)

		bf = cv2.BFMatcher()
		matches = bf.knnMatch(des1,des2, k=2)

		counter = 0
		mcounter=0
		good = []
		for m,n in matches:
		    if m.distance < 0.75*n.distance:
		        good.append([m])
		        counter+=1
			mcounter+=1

		img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
		valf = counter/(c1*1.0)
		tag = 'No Match'

		if (val>=0.95) and (val<=1):
			if (valf>=0.09):
				tag = 'Almost Same'

		elif (val>=0.70) and (val<=0.95):
			if (valf>=0.06):
				tag = 'Very Similar'

		elif (val>=0.52) and (val<=0.70):
			if (valf>=0.05):
				tag = 'Somewhat Similar'

		if (tag=='No Match'):
			if (valf>=0.08) and (val<=0.20):
				tag = 'Somewhat Similar'
			elif (valf>=0.2):
				tag = 'Very Similar'
		
		print "File Name: ",file1
		print "Status: ",tag
		print "Correlation Value: ",val
		print "Feature Matching: ",valf

		cv2.imshow(pa1,image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print



