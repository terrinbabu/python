from scipy.spatial import distance as dist
import argparse
import numpy as np
import cv2
import imutils
from imutils import contours
import time

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def order_points(pts):
    xSorted = pts[np.argsort(pts[:, 0]), :]
    leftMost = xSorted[:2, :]
    rightMost = xSorted[2:, :]
    leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
    (tl, bl) = leftMost
    D = dist.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
    (br, tr) = rightMost[np.argsort(D)[::-1], :]
    return np.array([tl, tr, br, bl], dtype="float32")

image = cv2.imread("object_measurement.jpg")  # load our input image, convert it to grayscale, and blur it slightly
image = rescale_frame(image, percent=15)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
edged = cv2.Canny(gray, 50, 100) # perform edge detection, then perform a dilation + erosion to close gaps in between object edges
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # find contours in the edged image
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
(cnts, _) = contours.sort_contours(cnts) # sort the contours from left-to-right

colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0)) #initialize the bounding box point colors
object_num = 0

for (i, c) in enumerate(cnts): # loop over the contours individually
    if cv2.contourArea(c) < 500:   # if the contour is not sufficiently large, ignore it
        continue
    
    box = cv2.minAreaRect(c)   # compute the rotated bounding box of the contour
    box = cv2.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    cv2.drawContours(image, [box], -1, (0, 255, 0), 2) # draw the contours
    
    object_num += 1
    print("Object #{}:".format(object_num))
    #print(box) # show the original coordinates

    rect = order_points(box) # order the points in the contour such that they appear in top-left, top-right, bottom-right, and bottom-left order
    print(rect.astype("int")) ## show the re-ordered coordinate
    print("")

    for ((x, y), color) in zip(rect, colors): # loop over the original points and draw them
        cv2.circle(image, (int(x), int(y)), 5, color, -1)
 
    cv2.putText(image, "Object #{}".format(object_num),(int(rect[0][0] - 15), int(rect[0][1] - 15)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2) # draw the object num at the top-left corner

while True:
    cv2.imshow("Image", image)
    if cv2.waitKey(20) & 0xFF == ord('c'):
        break
