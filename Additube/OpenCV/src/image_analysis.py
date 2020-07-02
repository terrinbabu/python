import numpy as np
import cv2
from imutils import perspective
from imutils import contours
import imutils

img = cv2.imread('NIR2_mask_img.png', 0)
#ret,thresh = cv2.threshold(img,127,255,0)
#contours,hierarchy = cv2.findContours(thresh, 1, 2)
#cnt = contours[0]

edged = cv2.Canny(img, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

#M = cv2.moments(cnts)
#print(M)

blank_image = np.zeros((edged.shape), np.uint8)

for (i, c) in enumerate(cnts): # loop over the contours individually
    if cv2.contourArea(c) < 100:
        continue
    
    hull = cv2.convexHull(c)
    cv2.polylines(blank_image,[hull],True,(255,255,255))
    #print(hull)

#print(hull)
#print(hull.ndim)

#hull = hull.ravel()

#print(hull.ndim)
#print(hull)
#hull = np.reshape(hull, (-1, 2))

#print(hull.ndim)
#print(hull)
#print(hull.dtype)

#hull = hull.reshape(-1,1,2)
#print(hull.ndim)
#print(hull)

##polygonal = np.array({})

#print(' start ')

#pts = np.array([[188, 140],[160,197],[140,209],[138,209]],np.int32)
#pts = pts.reshape(-1,1,2)

#print(polygonal.ndim)

#count = 0

#for i in hull:
    #print(i.ndim)
    #polygonal([count]) = i 
    #count += 1

#print(polygonal.shape)

#hull = hull.reshape((-1,1,2))
#print(hull.shape)

x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img,center,radius,(0,255,0),2)

ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(0,255,0),2)

while True:
    cv2.imshow('blank_image', blank_image)
    if cv2.waitKey(20) & 0xFF == ord('c'):
        break
