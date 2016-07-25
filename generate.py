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

root = 'Dataset/'

for subdir, dirs, files in os.walk(root):
	for file in files:
		pa = str(root) + str(file)
		img = cv2.imread(pa)
		s1,s2,s3 = img.shape
		# print s1, s2
		a1 = random.randint(100,150)
		a2 = random.randint(350,450)
		b1 = random.randint(200,350)
		b2 = random.randint(600,750)
		cropped = img[a1:a2, b1:b2]
		pa = 'Modified/' + 'magnified-' + str(file)
		# cv2.imshow(pa,cropped)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()
		res = cv2.resize(img,(1440, 810), interpolation = cv2.INTER_CUBIC)
		# cv2.imshow(pa,cropped)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()
		cv2.imwrite(pa,res)
		# print rcParams

