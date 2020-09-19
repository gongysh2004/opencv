# Shape and Texts

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)  # '0' means Black, 512 height and weight
print(img.shape)
img[:] = 0,0,0   #RGB

#cv2.line(img,(0,0),(300,300),(0,255,0),3)  # 3 = for thickness
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)  # 3 = for thickness
cv2.rectangle(img,(0,0),(250,350),(255,0,0),cv2.FILLED) # 'cv2.FILLED' for fill the color in shape or 3 thikness
cv2.circle(img,(450,60),30,(255,255,0),1)
cv2.putText(img, "OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,125,234),1) # 1 for scale size of font

cv2.imshow("image",img)

cv2.waitKey(0)