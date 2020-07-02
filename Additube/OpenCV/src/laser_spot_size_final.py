from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)    

my_cap = cv2.VideoCapture('NIR2_gray.avi')
frame_counter = 0

while True:
    
    ret, frame_real = my_cap.read()
    frame_cropped = rescale_frame(frame_real, percent=50)
    frame_cropped = frame_cropped[0:300, 140:430]
    frame_hsv = cv2.cvtColor(frame_cropped, cv2.COLOR_BGR2HSV)

    lower_filter = np.array([0,0,168]) # 160 for NIR1 and 168 for NIR2
    upper_filter = np.array([0,0,255])
    
    my_mask = cv2.inRange(frame_hsv, lower_filter, upper_filter)
    my_result = cv2.bitwise_and(frame_cropped, frame_cropped, my_mask, my_mask)
    
    edged = cv2.Canny(my_result, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    for (i, c) in enumerate(cnts): # loop over the contours individually
        if cv2.contourArea(c) < 1000:
            continue
        
        ellipse = cv2.fitEllipse(c) #[(x coordinate of the center,y coordinate of the center),(major semi-axis,minor semi-axis),rotation angle ]
        print(ellipse[1][0])
        cv2.ellipse(frame_cropped,ellipse,(255,255,255),2)
    
    cv2.imshow('frame_cropped', frame_cropped)
    
    frame_counter += 1                                                  #
    if frame_counter == my_cap.get(cv2.CAP_PROP_FRAME_COUNT):           #
        frame_counter = 0                                               # to loop the video till you stop it
        my_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)                          #

    if cv2.waitKey(20) & 0xFF == ord('c'):
        break

my_cap.release()
cv2.destroyAllWindows()
