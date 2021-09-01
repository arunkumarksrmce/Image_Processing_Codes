# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:46:37 2021

@author: CRI
"""
import pickle
import cv2
im = cv2.imread('test.png')
image = {
    #'pixels': im.tostring(),
    'size': im.size,
    #'mode': im.mode,
}

# # Write to file.
# file = open("data.pkl", "wb")
# pickle.dump(image, file)
# #pickle.dump(image2, file)
# file.close()

# # # Read from file.
# file = open("data.pkl", "rb")
# im1 = pickle.load(file)
# # #image2 = pickle.load(file)
# # file.close()
# # # Pickle dictionary using protocol 0.
# # pickle.dump(image, file)
# # file.close()