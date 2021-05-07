# Basic functions

import cv2
import numpy as np
img = cv2.imread("Source/elon musk.jpg")
cv2.resize()
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # number must be odd
imgCanny = cv2.Canny(img, 100,100) # threshold values, more munber less edges
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1 ) # We use matrix to increase thickness in img edges, increate in iteration dramatic thick ness changes
imgErode = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("image gray", imgGray)
cv2.imshow("image Blur", imgBlur)
cv2.imshow("image Canny", imgCanny)
cv2.imshow("image CannyDilation", imgDilation)
cv2.imshow("image Erode", imgErode)
cv2.waitKey(0)