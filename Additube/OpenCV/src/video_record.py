import os
import numpy as np
import cv2

# opencv is not used to record audio #use ffmpeg for recording audio

# dictionary

STD_DIMENSIONS =  {     #  defining some standard Video Dimensions Sizes
    '480p': (640, 480),
    '720p': (1280, 720),
    '1080p': (1920, 1080),
    '4k': (3840, 2160),
}

VIDEO_TYPE = {           # Video Encoding, might require additional installs
    'avi': cv2.VideoWriter_fourcc(*'XVID'),  # Types of Codes: http://www.fourcc.org/codecs.php #XVID works very well on avi and mp4 for windows
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

# definitions

def change_res(cap,width, height):
    cap.set(3, width)
    cap.set(4, height)
    
def get_dims(cap, res='1080p'):              # if resolution is not defined then resolution by 
    width, height = STD_DIMENSIONS['480p']   # if an error in defining the resolution then it will be 480p by default
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cap,width,height)
    return width,height

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

# my program

my_filename = 'NIR2_convert_gray.mp4'   # .avi , .mp4
my_frames_per_seconds = 24.0        # typical movie's fps
my_res = '480p'                     # req. resoulution 480p,720p,1080p,4k

my_cap = cv2.VideoCapture('NIR2_convert.avi')      
my_dims = get_dims(my_cap, res=my_res)
my_video_type = get_video_type(my_filename)
my_output = cv2.VideoWriter(my_filename,my_video_type,my_frames_per_seconds,my_dims) # you can put (width,height) instead of (dims)

while True:                      
    
    ret, frame_real = my_cap.read()
    frame_gray = cv2.cvtColor(frame_real, cv2.COLOR_BGR2GRAY)
    
    my_output.write(frame_gray)
    cv2.imshow('frame_gray', frame_gray)
    
    if cv2.waitKey(20) & 0xFF == ord('c'): 
        break

my_cap.release()
my_output.release()
cv2.destroyAllWindows()
