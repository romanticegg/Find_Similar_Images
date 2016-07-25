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

img1 = cv2.imread('Cropped/crop-outdoor-s1-00996.jpg',0)          # queryImage

root = 'Dataset/'

for subdir, dirs, files in os.walk(root):
	for file in files:
		pa = str(root) + str(file)
		img2 = cv2.imread(pa)
		# img2 = cv2.imread('Dataset/cofee-s1-00186.jpg',0) # trainImage

		# Initiate SIFT detector
		sift = cv2.xfeatures2d.SIFT_create()

		# find the keypoints and descriptors with SIFT
		kp1, des1 = sift.detectAndCompute(img1,None)
		kp2, des2 = sift.detectAndCompute(img2,None)

		c1 = len(kp1)
		c2 = len(kp2)
		print c1, c2
		bf = cv2.BFMatcher()
		matches = bf.knnMatch(des1,des2, k=2)
		# print matches

		# Apply ratio test
		counter = 0
		good = []
		for m,n in matches:
		    if m.distance < 0.75*n.distance:
		        good.append([m])
		        counter+=1

		# cv2.drawMatchesKnn expects list of lists as matches.
		img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
		print file, " matches = ",counter
		plt.imshow(img3),plt.show()



		# # FLANN parameters
		# FLANN_INDEX_KDTREE = 0
		# index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
		# search_params = dict(checks=50)   # or pass empty dictionary

		# flann = cv2.FlannBasedMatcher(index_params,search_params)

		# matches = flann.knnMatch(des1,des2,k=2)


		# # Need to draw only good matches, so create a mask
		# matchesMask = [[0,0] for i in xrange(len(matches))]

		# # ratio test as per Lowe's paper
		# for i,(m,n) in enumerate(matches):
		#     if m.distance < 0.7*n.distance:
		#         matchesMask[i]=[1,0]

		# print matchesMask

		# draw_params = dict(matchColor = (0,255,0),
		#                    singlePointColor = (255,0,0),
		#                    matchesMask = matchesMask,
		#                    flags = 0)

		# img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

		# plt.imshow(img3,),plt.show()

