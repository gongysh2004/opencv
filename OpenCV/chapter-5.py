# WARP PRESPECTIVE

import cv2
import numpy as np

width,height = 250, 350

img = cv2.imread("Source/card1.jpg")
pts1 = np.float32([[445,180],[614,255],[335,436],[496,513]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("image",img)
cv2.imshow("output",imgoutput)

cv2.waitKey(0)

