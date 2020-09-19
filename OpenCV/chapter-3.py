# Resizing and Cropping
 
import cv2
import numpy as np


img = cv2.imread("Resources/elon musk.jpg")
print(img.shape) #output (height, weight, 3=chnnel BGR)

imgresize = cv2.resize(img,(400,300)) #(weight,hieght)
print(imgresize.shape)

imgCropped = img[0:300,300:600]

cv2.imshow("leaf",img)
cv2.imshow("leaf resize", imgresize)
cv2.imshow("leaf cropped", imgCropped)

cv2.waitKey(0)