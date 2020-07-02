# This program is used to create a face recoginzer trainer and its labels

import os
from PIL import Image
import numpy as np
import cv2
import pickle

#### cascade and recognizer ####

my_face_cascade = cv2.CascadeClassifier('C:\\Users\\terrin\\dev\\OpenCV\\cascades\\data\\haarcascade_frontalface_alt2.xml')
my_recognizer = cv2.face.LBPHFaceRecognizer_create() #using LBPH face recoginzer there is a lot of them but this one works fine


#### variables declared to be used inside a loop ####

current_id = 0
face_image_label = 0
label_ids = {}  # an empty dict
x_train = []
y_labels = []


#### search for face images in specific folders ####

MY_BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #path directory of this python file
my_image_dir = os.path.join(MY_BASE_DIR,"images") #add image folder name to the path

for my_root, my_dirs, my_files in os.walk(my_image_dir):
    for my_file in my_files:
        if my_file.endswith("png") or my_file.endswith("jpg"):  # for each image
            
            my_path = os.path.join(my_root, my_file)  # image path
            
            #### create label dictionary with label name and id numbers ####
            
            my_label = os.path.basename(my_root).replace(" ","-").lower() #creating lable using the folder name
            
            if not my_label in label_ids:    # creating the label ids dict
                label_ids[my_label] = current_id
                current_id += 1
            
            #### convert the images into numpy arrays and face identification of that numpy array ####
            
            my_pil_image = Image.open(my_path).convert("L") #to make it gray scale
            re_size = (550, 550)
            my_final_image = my_pil_image.resize(re_size, Image.ANTIALIAS) # re size all the image to a particular size 
            
            my_image_array = np.array(my_final_image, "uint8") #every pixel into numpy array - image into numbers
            
            faces = my_face_cascade.detectMultiScale(my_image_array, scaleFactor=1.5, minNeighbors=5)    # detect the faces on the image
            
            #### create 2 arrays of face roi and its corresponding id number ####
            
            id_ = label_ids[my_label]
            
            for (x,y,w,h) in faces:  
                my_roi = my_image_array[y:y+h, x:x+w]
                x_train.append(my_roi)
                y_labels.append(id_)
                
                image_name = str(face_image_label) + "_" + str(id_) + ".png"    #
                cv2.imwrite(image_name,my_roi)                                  # to check if the roi and id numbers are matching
                face_image_label += 1                                           #

print(label_ids)

#### Train the OpenCV recognizer using the two arrays created ####	

my_recognizer.train(x_train, np.array(y_labels)) # to train the recognizer also change the labels into numpy arrays
my_recognizer.save("my_trainer.yml") 
            
#### save the label dictionary created into a pickle file ####

with open("my_face_labels_ids.pickle",'wb') as f: #wb - writing bytes as f - files
    pickle.dump(label_ids, f)  # put label ids into a file
