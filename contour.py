import numpy as np
import cv2 as cv

img = cv.imread('roof.jpg',0)
ret, thresh = cv.threshold(img,127,255,0)
contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#im2, contours, hierarchy = cv.findContours(thresh,1,2)
cnt = contours[0]
M = cv.moments(cnt)
print(M)
if M['m00']!=0:
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

area = cv.contourArea(cnt)
perimeter = cv.arcLength(cnt,True)

epsilon = 0.1 * cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)