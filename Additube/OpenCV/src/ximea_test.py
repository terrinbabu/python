from ximea import xiapi
import cv2
import matplotlib.pyplot as plt
import socket
import numpy as np

# to increase the USB buffer size : $sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb >/dev/null <<<0

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
  
cam = xiapi.Camera()
cam.open_device()
cam.set_exposure(20000)

img = xiapi.Image()

cam.start_acquisition()

frame_counter_wo = 0
x_frame_counter_wo = []
y_laser_spot_length = []
contour_area_limit = 3000

#host = '127.0.0.1'
#port = 5000
#s = socket.socket()
#s.connect((host,port))

def nothing(x):                                                            #
   pass                                                                    #
cv2.namedWindow("Trackbars")                                               #
cv2.createTrackbar("Lower_limit","Trackbars", 0, 255, nothing)             # to find the upper and lower filter (1/2)
cv2.createTrackbar("Upper_limit","Trackbars", 0, 255, nothing)             #

try:
    while True:
      
        cam.get_image(img) #get data and pass them from camera to img
        
        data = img.get_image_data_numpy() #create numpy array with data from camera. Dimensions of the array are determined by imgdataformat
        #cv2.imshow('XiCAM example', data)
	
        frame_cropped = rescale_frame(data, percent=50)
	cv2.imshow('frame_cropped', frame_cropped)
	
	l = cv2.getTrackbarPos("Lower_limit", "Trackbars")                            #
	u = cv2.getTrackbarPos("Upper_limit", "Trackbars")                            # to find the upper and lower filter (2/2)
	lower_filter = np.array([l])        			                      #
	upper_filter = np.array([u])                                 		      #
	
	#lower_filter = np.array([0])
	#upper_filter = np.array([14])
	
	my_mask = cv2.inRange(frame_cropped, lower_filter, upper_filter)
	cv2.imshow('my_mask', my_mask)
	#my_result = cv2.bitwise_and(frame_cropped, frame_cropped, my_mask, my_mask)
	#cv2.imshow('my_result', my_result)
	
	edged = cv2.Canny(my_mask, 50, 100)
	edged = cv2.dilate(edged, None, iterations=1)
	edged = cv2.erode(edged, None, iterations=1)
	cv2.imshow('edged', edged)
	
	cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[1]
	
	blank_image = np.zeros((frame_cropped.shape), np.uint8)
	laser_spot_length = 0
	
	for (i, c) in enumerate(cnts): # loop over the contours individually
	    if cv2.contourArea(c) < contour_area_limit:
		continue
	    #print(cv2.contourArea(c))
	    
	    ellipse = cv2.fitEllipse(c) #[(x coordinate of the center,y coordinate of the center),(major semi-axis,minor semi-axis),rotation angle ]
	    cv2.ellipse(blank_image,ellipse,(255,255,255),2)
	    cv2.ellipse(frame_cropped,ellipse,(255,255,255),2)
	    laser_spot_length = ellipse[1][0]
	    
	    #(x,y),radius = cv2.minEnclosingCircle(c)
	    #center = (int(x),int(y))
	    #radius = int(radius)
	    #cv2.circle(blank_image,center,radius,(255,255,255),2)
	    #cv2.circle(frame_cropped,center,radius,(255,255,255),2)
	    #laser_spot_length = radius
	    
	#cv2.imshow('final_contour', blank_image)
	cv2.imshow('frame_with_contour', frame_cropped)
	
	print(laser_spot_length)
	#laser_spot_length_str = str(laser_spot_length)
	#s.send(laser_spot_length_str)
	y_laser_spot_length.append(laser_spot_length)

	frame_counter_wo += 1
	x_frame_counter_wo.append(frame_counter_wo)
	
	if cv2.waitKey(20) & 0xFF == ord('c'):
	    break
        
        
except KeyboardInterrupt:
    cv2.destroyAllWindows()

plt.plot(x_frame_counter_wo, y_laser_spot_length)
plt.ylabel('laser_spot_width (pixel_length)')
plt.xlabel('Time (frame counter)')
plt.show()

cam.stop_acquisition()
cam.close_device()
