
import cv2
import numpy as np

img = cv2.imread('Lenna.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)

cv2.imshow('Original', img)
cv2.imshow("H S V Separadas", hsv_split)

cv2.waitKey()
