# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:03:24 2021

@author: CRI
"""
import glob
import numpy as np
import cv2
X_data = []
files = glob.glob (r"C:\Users\CRI\Desktop\Dataset\Test\1\*.JPG")
for myFile in files:
    print('hi')
    image = cv2.imread (myFile)
    X_data.append (image)

print('X_data shape:', np.array(X_data).shape)