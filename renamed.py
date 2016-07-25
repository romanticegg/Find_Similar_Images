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
import csv
import time

root = 'EGO-GROUP/'
d = set()
for subdir, dirs, files in os.walk(root):
	for file in files:
		w,w1 = os.path.split(subdir)
		q,q1 = os.path.split(w)
		s = str(subdir) + '/' + str(q1) + '-' + str(w1) + '-' + str(file)
		original = str(subdir) + '/' + str(file)
		os.rename(original, s)
		print s
		d.add(os.path.join(subdir))

print d

