# this program is used to do face, eyes and smile identification and face recognizer using an existing face recognizer, trainer and its face labels

import numpy as np
import cv2
import pickle

#### cascade and recognizer ####

my_face_cascade = cv2.CascadeClassifier('C:\\Users\\terrin\\dev\\OpenCV\\cascades\\data\\haarcascade_frontalface_alt2.xml')
my_eye_cascade = cv2.CascadeClassifier('C:\\Users\\terrin\\dev\\OpenCV\\cascades\\data\\haarcascade_eye.xml')
my_smile_cascade = cv2.CascadeClassifier('C:\\Users\\terrin\\dev\\OpenCV\\cascades\\data\\haarcascade_smile.xml')

my_recognizer = cv2.face.LBPHFaceRecognizer_create()
my_recognizer.read("my_trainer.yml")    # reading an existing recognizer

#### creating face label dictionary ###

my_face_labels_org = {}  # empty dic
my_face_labels = {}

with open("my_face_labels_ids.pickle",'rb') as f: # rb - read bytes
    my_face_labels_org = pickle.load(f)
    my_face_labels = {v:k for k,v in my_face_labels_org.items()}  # inverting the dictionary ie. orginally it was {person name : id_num} now it will be {id_num : person_name}

#### capture video ####

my_cap = cv2.VideoCapture(0)

while(True):
    
    ret, frame_real = my_cap.read()
    
    #### face identification ####
    
    frame_gray = cv2.cvtColor(frame_real, cv2.COLOR_BGR2GRAY)     # cascade works only in gray frame scale

    all_faces = my_face_cascade.detectMultiScale(frame_gray, scaleFactor=1.5, minNeighbors=5) # detect all faces, increasing the scale factor makes it more accurate but not too much which can give some problem
    
    for (x,y,w,h) in all_faces:         # location of the faces (x cord, y cord, width, height)               
        
        my_roi_colour = frame_real[y:y+h, x:x+w] # roi = region of interest # (y_start:y_end , x_start:x_end)
        my_roi_gray = frame_gray[y:y+h, x:x+w]
        
        #my_gray_face_img_file = "my_face_gray.png"
        #cv2.imwrite(my_gray_face_img_file, my_roi_colour )   # take image of the face
    
        #### draw a rectangle on the identified face ###
    
        border_color = (255,0,0) # BGR - blue green red value from 0 to 255
        border_stroke = 2
        rectangle_width = x+w # actually its the ending cordinates of x
        rectangle_height = y+h # ending cordinates of y
        
        cv2.rectangle(frame_real, (x,y),(rectangle_width,rectangle_height), border_color, border_stroke ) # put a rectangle on the roi (frame , (starting x and y cordinates), (width and height), color, stroke)
        
        #### eyes and smile identification ####
        
        eyes = my_eye_cascade.detectMultiScale(my_roi_gray)
        for (ex,ey,ew,eh) in eyes:
           cv2.rectangle(my_roi_colour, (ex,ey),(ex+ew,ey+eh), (0,255,0),1) 
        
        smiles = my_smile_cascade.detectMultiScale(my_roi_gray)
        for (sx,sy,sw,sh) in smiles:
           cv2.rectangle(my_roi_colour, (sx,sy),(sx+sw,sy+sh), (0,0,255),1)
           
        #### face recognizer ####
    
        my_id_num,my_confidence = my_recognizer.predict(my_roi_gray) # the recognizer predicts the face with an id and confidence level - this is not actually      between 0 to 100 and not so sure what it is 
        
        if my_confidence >= 45:
            #print(my_id_num) # should give the id number of the face
            #print(my_face_labels[my_id_num]) # gives the name of the face
            
            #### display the name of the face on the frame ####
            
            label_font = cv2.FONT_HERSHEY_SIMPLEX
            label_name = my_face_labels[my_id_num]
            label_color = (0, 0, 0)
            label_stroke = 1
            label_font_size = 0.75
            
            cv2.putText(frame_real, label_name, (x,y), label_font, label_font_size, label_color, label_stroke, cv2.LINE_AA) # person name on the frame 

           
    cv2.imshow('frame_real',frame_real)
    
    if cv2.waitKey(20) & 0xFF == ord('c'):
        break
    
my_cap.release()
cv2.destroyAllWindows()
