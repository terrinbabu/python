import numpy as np
import cv2
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)       

#def nothing(x):                                                            #
   #pass                                                                    #
                                                                            
#cv2.namedWindow("Trackbars")                                               #
                                                                            
#cv2.createTrackbar("L-H","Trackbars", 0, 179, nothing)                     # to find the upper and lower filter (1/2)
#cv2.createTrackbar("L-S","Trackbars", 0, 255, nothing)                     # 
#cv2.createTrackbar("L-V","Trackbars", 0, 255, nothing)                     #
#cv2.createTrackbar("U-H","Trackbars", 0, 179, nothing)                     #
#cv2.createTrackbar("U-S","Trackbars", 0, 255, nothing)                     #
#cv2.createTrackbar("U-V","Trackbars", 0, 255, nothing)                     #

my_cap = cv2.VideoCapture('NIR1_gray.avi')
frame_counter = 0
frame_counter_wo = 0
x_frame_counter_wo = []
color_pix = np.arange(256)
y_gray_pix_array_of_arrays = {}

while True:
    

    ret, frame_real = my_cap.read()
    frame_cropped = rescale_frame(frame_real, percent=50)
    frame_cropped = frame_cropped[0:310, 140:430]
    
    frame_hsv = cv2.cvtColor(frame_cropped, cv2.COLOR_BGR2HSV) # HSV - Hue Saturation Value (Hue tells mainly the colour)
    
    #l_h = cv2.getTrackbarPos("L-H", "Trackbars")                           #
    #l_s = cv2.getTrackbarPos("L-S", "Trackbars")                           #
    #l_v = cv2.getTrackbarPos("L-V", "Trackbars")                           #
    #u_h = cv2.getTrackbarPos("U-H", "Trackbars")                           #
    #u_s = cv2.getTrackbarPos("U-S", "Trackbars")                           # to find the upper and lower filter (2/2)
    #u_v = cv2.getTrackbarPos("U-V", "Trackbars")                           #
                                                                            
    #lower_filter = np.array([l_h,l_s,l_v])                                 #
    #upper_filter = np.array([u_h,u_s,u_v])                                 #
    
    lower_filter = np.array([0,0,160]) # 160 for NIR1 and 168 for NIR2
    upper_filter = np.array([0,0,255])
    
    my_mask = cv2.inRange(frame_hsv, lower_filter, upper_filter)
    my_result = cv2.bitwise_and(frame_cropped, frame_cropped, my_mask, my_mask)

    #my_mask_img_file = "my_mask_img.png"
    #cv2.imwrite(my_mask_img_file, my_mask )   # take image of the face
    
    
    x_frame_counter_wo.append(frame_counter_wo)
    
    
    #gray_pix_array = []
    for i in color_pix.flat:
        n_gray_pix = np.sum(my_result == i)
        y_gray_pix_array_of_arrays[i,frame_counter_wo]=n_gray_pix
    
    frame_counter_wo += 1
    
    #print(len(gray_pix_array))
    
    #y_gray_pix_array_of_arrays.append(gray_pix_array)
    #print(len(y_gray_pix_array_of_arrays))
    
    cv2.imshow('frame_cropped', frame_cropped)
    cv2.imshow('my_mask', my_mask)
    cv2.imshow('my_result', my_result)
    
    frame_counter += 1                                                   #
    if frame_counter == my_cap.get(cv2.CAP_PROP_FRAME_COUNT):            #
        #frame_counter = 0                                               # to loop the video till you stop it
        #my_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)                          #
        print(len(y_gray_pix_array_of_arrays))
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x_frame_counter_wo, y_gray_pix_array_of_arrays,color_pix)

    if cv2.waitKey(20) & 0xFF == ord('c'):
        break

#ax.scatter(x_frame_counter_wo, y_gray_pix_array_of_arrays, color_pix, marker='o')
#print(y_gray_pix_array_of_arrays.shape)

#plt.plot(x_frame_counter_wo, y_gray_pix_array_of_arrays)

#plt.ylabel('Intensity (pixels)')
#plt.xlabel('Time (frame counter)')
#plt.show()

my_cap.release()
cv2.destroyAllWindows()
