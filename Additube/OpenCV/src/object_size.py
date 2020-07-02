from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
 
def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def order_points(pts):
    xSorted = pts[np.argsort(pts[:, 0]), :]
    
    leftMost = xSorted[:2, :]
    rightMost = xSorted[2:, :]
    
    leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
    (tl, bl) = leftMost
    
    D = dist.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
    (br, tr) = rightMost[np.argsort(D)[::-1], :]

    return np.array([tl, tr, br, bl], dtype="float32")

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

ap = argparse.ArgumentParser() # construct the argument parse and parse the arguments
ap.add_argument("-i", "--image", required=True, help="path to the input image")
ap.add_argument("-w", "--width", type=float, required=True, help="width of the left-most object in the image (in cm)")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = rescale_frame(image, percent=15)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
(cnts, _) = contours.sort_contours(cnts)

pixelsPerMetric = None
object_num = 0

for (i, c) in enumerate(cnts): # loop over the contours individually
    if cv2.contourArea(c) < 500:
        continue

    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = order_points(box)
    #cv2.drawContours(image, [box.astype("int")], -1, (0, 255, 0), 2) # draw the object border on the image

    #for (x, y) in box:    # draw corner points on the image
        #cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)

    (tl, tr, br, bl) = box            
    (tltrX, tltrY) = midpoint(tl, tr) # midpoint of top left and top right cordinates and so on
    (blbrX, blbrY) = midpoint(bl, br)
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)

    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY)) # compute the Euclidean distance between the midpoints
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

    if pixelsPerMetric is None: # if the pixels per metric has not been initialized, thencompute it as the ratio of pixels to supplied metric
        pixelsPerMetric = dB / args["width"] 

    dimA = dA / pixelsPerMetric # compute the size of the object
    dimB = dB / pixelsPerMetric
    
    #cv2.circle(image, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1) 	# draw the midpoints on the image
    #cv2.circle(image, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
    #cv2.circle(image, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
    #cv2.circle(image, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
 
    cv2.line(image, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),(255, 0, 255), 2) 	# draw lines between the midpoints
    cv2.line(image, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),(255, 0, 255), 2)
    
    #cv2.putText(image, "{:.1f}cm".format(dimA),(int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,0.65, (255, 255, 255), 2) #object sizes on the image
    #cv2.putText(image, "{:.1f}cm".format(dimB),(int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,0.65, (255, 255, 255), 2)
    
    object_num += 1
    print("Object #{}:".format(object_num))
    print("dimension 1:{:.2f}cm".format(dimA))
    print("dimension 2:{:.2f}cm".format(dimB))
    cv2.putText(image, "Object #{}".format(object_num),(int(box[0][0] - 15), int(box[0][1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)
    
    
while True:
    cv2.imshow("Image", image)
    if cv2.waitKey(20) & 0xFF == ord('c'):
        break
