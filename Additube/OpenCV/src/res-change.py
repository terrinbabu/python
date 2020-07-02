import numpy as np
import cv2

# input required for definitions

my_cap = cv2.VideoCapture(0)

# definitions

def make_1080p():     # some predefined resolution, here its 1080p           
    my_cap.set(3, 1920)  # 3 for width and 4 for height 
    my_cap.set(4, 1080)

def make_720p():      # some predefined resolution, here its 1080p  
    my_cap.set(3, 1280)
    my_cap.set(4, 720)

def make_480p():      # some predefined resolution, here its 1080p  
    my_cap.set(3, 640)
    my_cap.set(4, 480)

def change_res(width,height):  # choose the width and height of your preference
    my_cap.set(3, width)
    my_cap.set(4, height)

def rescale_frame(frame, percent=75):    # to rescale a frame
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


# my program


#change_res(400,200)  # to define your own resolution
#make_720p()           # use the predefined resolution

while True:                     

    ret, frame_real = my_cap.read()
    
    frame_resized_30 = rescale_frame(frame_real, percent=30)              # using rescale_frame defintion
    frame_resized_140 = rescale_frame(frame_real, percent=140)
    
    cv2.imshow('frame_resized_30', frame_resized_30)   
    cv2.imshow('frame_resized_140', frame_resized_140)   
    
    if cv2.waitKey(20) & 0xFF == ord('c'):
        break
    
my_cap.release() 
cv2.destroyAllWindows()
