# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:59:27 2020

@author: harsh
"""

# FACE DETECTION, DEMARCATION
import cv2
    
def face_det(path):
    # load the photograph
    pixels = cv2.imread(path)
    
    # load the pre-trained model
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    # perform face detection
    bboxes = classifier.detectMultiScale(pixels)
    
    # print bounding box for each detected face
    for box in bboxes:
    	#print(box)
        # extract
    	x, y, width, height = box
    	x2, y2 = x + width, y + height
    	# draw a rectangle over the pixels
    	cv2.rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
    
    # show the image
    #cv2.imshow('face detection', pixels)

    # keep the window open until we press a key
    #cv2.waitKey(0)
    
    # close the window
    #cv2.destroyAllWindows() 
    pad(box) 
    
face_det("C:\\Users\harsh\\Documents\\Programming\\PROJECTS\\BEProj_Enhanced_ATM\\codes\\image1_29.jpg") 

def pad(face_dims):
    print(face_dims) 