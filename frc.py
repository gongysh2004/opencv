import cv2
import numpy as np
import time
path = "frc.jpg"
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
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
        return (top_left, bottom_right)

def getContour(img):
    contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contour = sorted(contour, key=cv2.contourArea, reverse=True)
    contour=contour[0:1]
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
        cv2.circle(imgContour, (x+w//2,y), 5, [0,0,255], 2)
        #cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,0,255),2)


img = cv2.imread(path)
ts = time.time()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = cv2.inRange(imgGray, 252, 255)
res = cv2.bitwise_and(imgGray,imgGray, mask= mask)

imgContour=img.copy()
getContour(res)
ts2 = time.time()
print("time: %.5f" % (ts2-ts))
stackImg = stackImages(0.6, ([img, res,imgContour]))
cv2.imshow("img", stackImg)
while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break