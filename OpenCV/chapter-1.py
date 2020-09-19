''' How to read images, videos, and webcam '''

import cv2



'''
# live web cam its similar to video capturing
cap = cv2.VideoCapture(0)
cap.set(3,640) # width(id, pixel)
cap.set(4,480) # height(id, pixel)
cap.set(10,100) # adjust brightness
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): # press q to quit
        break

'''

'''
#import video 

cap = cv2.VideoCapture("Resources/testvideo/test.mp4")

    #video is set of images thats why we use while loop

while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): # press q to quit
        break

'''


'''
#import image

print("done")

img = cv2.imread("Resources/known/elon musk.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)   # 0 means infinity waiting time and 1000 == 1 second

'''