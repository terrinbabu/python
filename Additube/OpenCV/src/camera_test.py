import numpy as np
import cv2

my_cap = cv2.VideoCapture(0)        #capture video from the default capturing device

while True:                      # infinte running while loop to continously read what is in the video
    
    ret, frame_real = my_cap.read()      # reading frame by frame
    
    frame_gray = cv2.cvtColor(frame_real, cv2.COLOR_BGR2GRAY) # convert frame_real to gray colourù
    
    cv2.imshow('frame_real', frame_real)   # show what is reading
    cv2.imshow('frame_gray', frame_gray)
    
    if cv2.waitKey(20) & 0xFF == ord('c'):     # press c to close and solves the problem with gray bar appearence
        break
