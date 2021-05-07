import cv2
import os
import numpy as np
from pathlib import Path
import glob



cv_img = []
cv_img_names =[]
for img in glob.glob("imgs/*.jpg"):
    n= cv2.imread(img)
    cv_img.append(n)
    cv_img_names.append(img[5:])

def search_target():
    template = cv2.imread('template.png')
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.inRange(template, 252, 255)
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF',
                #'cv2.TM_CCOEFF_NORMED',
                #'cv2.TM_CCORR',
                #'cv2.TM_CCORR_NORMED', 
                #'cv2.TM_SQDIFF',  #BAD
                #'cv2.TM_SQDIFF_NORMED',  #BAD
                ]
    for meth in methods:
        method = eval(meth)
        # Apply template Matching
        res = cv2.matchTemplate(imgGray,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        return (top_left[0],top_left[1], bottom_right[0],bottom_right[1])


def isInRect(rect, point):
    print("rect: x1 %d:y1 %d:x2 %d:y2 %d" % rect)
    print("point: x %d:y %d" % point)
    return point[0]>=rect[0] and point[0] <=rect[2] and point[1]>=rect[1] and point[1] <=rect[3]

def getContour(img,imgContour):
    contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contour = sorted(contour, key=cv2.contourArea, reverse=True)

    contour=[ cnt for cnt in contour if cv2.contourArea(cnt)>100  ]
    for cnt in contour:
        # hull = cv2.convexHull(cnt,returnPoints = False)
        # defects = cv2.convexityDefects(cnt,hull)
        # if defects is not None:
        #     for i in range(defects.shape[0]):
        #         s,e,f,d = defects[i,0]
        #         start = tuple(cnt[s][0])
        #         end = tuple(cnt[e][0])
        #         far = tuple(cnt[f][0])
        #         cv2.line(imgContour,start,end,[0,255,0],2)
        #         cv2.circle(imgContour,far,5,[0,0,255],-1)

        #cv2.drawContours(imgContour, cnt, -1, (0,255,0), 1)
        x,y,w,h = cv2.boundingRect(cnt)
        rect = search_target()
        inFlag = isInRect(search_target(), (x+w//2,y))
        print("inFlag: %s\n" % str(inFlag))
        cv2.circle(imgContour, (x+w//2,y), 10, [0,0,255], 2)
        cv2.putText(imgContour, "%d:%d" % (x+w//2,y),
        (x+w//2,y),cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,255),2)
        cv2.rectangle(imgContour, (rect[0],rect[1]),(rect[1],rect[3]),(0,0,255),2)

index = 0
dirname = 'test'
Path(dirname).mkdir(exist_ok=True)
# os.mkdir(dirname,exist_ok=True)
for path in cv_img:
    img = path
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(imgGray, 252, 255)
    res = cv2.bitwise_and(imgGray,imgGray, mask= mask)
    imgContour=img.copy()
    print("filename: %s\n" %   cv_img_names[index])
    getContour(res,imgContour)
    cv2.imwrite(os.path.join(dirname, cv_img_names[index]),imgContour)
    index += 1
