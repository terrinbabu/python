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
white_color = [255,255,255]
frame_counter = 0
frame_counter_wo = 0
y_white_pix_array = []
x_frame_counter_wo = []
y_laser_spot_length = []

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
    
    #if cnts[0].size > 0:
        #(cnts, _) = contours.sort_contours(cnts)

    rows,cols = my_mask.shape
    blank_image = np.zeros((my_mask.shape), np.uint8)
    M = cv2.getRotationMatrix2D((cols/2,rows/2),315,1)  # rotate the image

    for (i, c) in enumerate(cnts): # loop over the contours individually
        if cv2.contourArea(c) < 1000:
            continue

        cv2.drawContours(blank_image, c, -1, white_color,2)
        
        hull = cv2.convexHull(c)
        cv2.polylines(blank_image,[hull],True,white_color)
        
        ellipse = cv2.fitEllipse(c)
        #cv2.ellipse(blank_image,ellipse,white_color,2)
        cv2.ellipse(my_result,ellipse,white_color,2)

        blank_image = cv2.warpAffine(blank_image,M,(cols,rows))     # to rotate the image

    indices = np.where(blank_image == [255])
    
    if indices[1].size > 0:
        min_x_white_px = indices[1].min()
        max_x_white_px = indices[1].max()
        length = max_x_white_px - min_x_white_px
        y_laser_spot_length.append(length)
    else:
        y_laser_spot_length.append(0)
    
    #print("length of the laser spot: {} pixel length".format(length))
    
    n_white_pix = np.sum(my_mask == 255)
    y_white_pix_array.append(n_white_pix)
    frame_counter_wo += 1
    x_frame_counter_wo.append(frame_counter_wo)
    
    cv2.imshow('frame_cropped', frame_cropped)
    cv2.imshow('my_mask', my_mask)
    cv2.imshow('my_result', my_result)
    cv2.imshow('blank_image', blank_image)
    
    frame_counter += 1                                                  #
    if frame_counter == my_cap.get(cv2.CAP_PROP_FRAME_COUNT):           #
        frame_counter = 0                                               # to loop the video till you stop it
        my_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)                          #

    if cv2.waitKey(20) & 0xFF == ord('c'):
        break

plt.plot(x_frame_counter_wo, y_white_pix_array)
plt.ylabel('Intensity (pixels)')
plt.xlabel('Time (frame counter)')
plt.show()

plt.plot(x_frame_counter_wo, y_laser_spot_length)
plt.ylabel('laser spot width (pixels_length)')
plt.xlabel('Time (frame counter)')
plt.show()

my_cap.release()
cv2.destroyAllWindows()
