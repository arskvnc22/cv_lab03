print('hello from lab3.py')
import cv2
import numpy as np
img = cv2.imread('data/robot_010.png', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3,3),np.float32)/9
img_conv = cv2.filter2D(img,-1,kernel)