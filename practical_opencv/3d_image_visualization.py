# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:22:24 2021

@author: nkele
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

img =cv2.imread("table_image.jpg", 1)
#print(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (160,120))

gray = cv2.blur(gray, (3,3))


# create grid to plot using numpy
xx, yy = np.mgrid[0:gray.shape[0], 0:gray.shape[1]]
# create the figure
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, gray ,rstride=1, cstride=1, cmap=plt.cm.gray,
 linewidth=1)
# show it
plt.show()










