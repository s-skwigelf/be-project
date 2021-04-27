# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:22:11 2021

@author: harsh
"""

# ------------------------ INTEGRATED CAM MODULES ----------------------------

import datetime
import os
from PIL import Image
import numpy as np
from keras.models import model_from_json
from scipy.ndimage import imread
from scipy.misc import imresize, imsave
import cv2
import face_recognition
from tqdm import tqdm
from collections import defaultdict
from imutils.video import VideoStream
from tensorflow.keras.models import load_model
import pyttsx3

IMG_SIZE = 24

#setting speech lines
l0 = "QR code reader initialized..."
l1 = "Please hold the QR Code in front of the camera."
l2 = "Card expired. Please contact your bank."
l3 = "Card verified. Please proceed."
l4 = "Spoof detection system initialized..."
l5 = "Please hold your face still in the camera."
l6 = "Face verified. Please proceed with the transaction."
l7 = "Spoof detected. This account will be blocked."

def say(line):
    engine = pyttsx3.init()
    engine.say(line)
    engine.runAndWait()

def init_cam():
    # initalize the cam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    print("Webcam started")
    QRscan_read(cap)
    go(cap)

def QRscan_read(cap):
    
    print("QR code reader initialized")
    say(l0)
    say(l1)
    
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    
    from luhn import luhn_algo
    while True:
        _, img = cap.read()
        #img = cv2.resize(img, None, fx=0.9, fy=0.9)
        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if bbox is not None:
            # display the image with lines
            for i in range(len(bbox)):
                # draw all lines
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
            if data:
                #print("[+] QR Code detected, data:", data)
                cno = data[0:15]                          # plus 1 from all
                card_from_date = data[17:22]              # numbers in lines
                card_exp_date = data[24:29]               # 31, 32 and 33
                #print(card_from_date)
                #print(card_exp_date)
                #print(cno)
                cfd = datetime.datetime.strptime(card_from_date, '%m/%y').date()
                ced = datetime.datetime.strptime(card_exp_date, '%m/%y').date() 
                cur = datetime.datetime.today().date() 
                
                if cur > ced:
                    #print("Card expired. Contact your bank")
                    say(l2)
                    terminate(cap)
                    break
                else:
                    #print("Card good")
                    say(l3)
                    luhn_algo(cno)
                    break
        #else:
        #    break
                
        # display the result
        display(img, cap)
        #cv2.imshow("img", img)    
        #if cv2.waitKey(1) == ord("q"):
        #    break
    #print(data)
    #cap.release()
    #cv2.destroyAllWindows()

def load_pretrained_model():
    model = load_model('eye_status_classifier0.h5')
    return model

def predict(img, model):
	img = Image.fromarray(img, 'RGB').convert('L')
	img = imresize(img, (IMG_SIZE,IMG_SIZE)).astype('float32')
	img /= 255
	img = img.reshape(1,IMG_SIZE,IMG_SIZE,1)
	prediction = model.predict(img)
	if prediction < 0.1:
		prediction = 'closed'
	elif prediction > 0.90:
		prediction = 'open'
	else:
		prediction = 'idk'
	return prediction

def init():
    face_cascPath = 'haarcascade_frontalface_alt.xml'
    #face_cascPath = 'lbpcascade_frontalface.xml'

    open_eye_cascPath = 'haarcascade_eye_tree_eyeglasses.xml'
    left_eye_cascPath = 'haarcascade_lefteye_2splits.xml'
    right_eye_cascPath ='haarcascade_righteye_2splits.xml'
    dataset = 'faces'

    face_detector = cv2.CascadeClassifier(face_cascPath)
    open_eyes_detector = cv2.CascadeClassifier(open_eye_cascPath)
    left_eye_detector = cv2.CascadeClassifier(left_eye_cascPath)
    right_eye_detector = cv2.CascadeClassifier(right_eye_cascPath)

    model = load_pretrained_model()

    print("[LOG] Collecting images ...")
    images = []
    for direc, _, files in tqdm(os.walk(dataset)):
        for file in files:
            if file.endswith("jpg"):
                images.append(os.path.join(direc,file))
    return (model,face_detector, open_eyes_detector, left_eye_detector,right_eye_detector, images)

def process_and_encode(images):
    # initialize the list of known encodings and known names
    known_encodings = []
    known_names = []
    #print("[LOG] Encoding faces ...")

    for image_path in tqdm(images):
        # Load image
        image = cv2.imread(image_path)
        # Convert it from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
     
        # detect face in the image and get its location (square boxes coordinates)
        boxes = face_recognition.face_locations(image, model='cnn')

        # Encode the face into a 128-d embeddings vector
        encoding = face_recognition.face_encodings(image, boxes)

        # the person's name is the name of the folder where the image comes from
        name = image_path.split(os.path.sep)[-2]

        if len(encoding) > 0 : 
            known_encodings.append(encoding[0])
            known_names.append(name)

        encodings = {"encodings": known_encodings, "names": known_names}
        np.save('encodings.npy', encodings) 

    return encodings

def isBlinking(history, maxFrames):
    """ @history: A string containing the history of eyes status 
         where a '1' means that the eyes were closed and '0' open.
        @maxFrames: The maximal number of successive frames where an eye is closed """
    for i in range(maxFrames):
        pattern = '1' + '0'*(i+1) + '1'
        if pattern in history:
            return True
    return False

def detect_and_display(model, video_capture, face_detector, open_eyes_detector, left_eye_detector, right_eye_detector, data, eyes_detected):
        _, frame = video_capture.read()
        # resize the frame
        frame = cv2.resize(frame, (0, 0), fx=0.9, fy=0.9)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect faces
        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(50, 50),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # for each detected face
        for (x,y,w,h) in faces:
            # Encode the face into a 128-d embeddings vector
            encoding = face_recognition.face_encodings(rgb, [(y, x+w, y+h, x)])[0]

            # For now we don't know the person name
            name = "Unknown"

            face = frame[y:y+h,x:x+w]
            gray_face = gray[y:y+h,x:x+w]

            eyes = []
            
            # Eyes detection
            # check first if eyes are open (with glasses taking into account)
            open_eyes_glasses = open_eyes_detector.detectMultiScale(
                gray_face,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
            # if open_eyes_glasses detect eyes then they are open 
            if len(open_eyes_glasses) == 2:
                eyes_detected[name]+='1'
                for (ex,ey,ew,eh) in open_eyes_glasses:
                    cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
            # otherwise try detecting eyes using left and right_eye_detector
            # which can detect open and closed eyes                
            else:
                # separate the face into left and right sides
                left_face = frame[y:y+h, x+int(w/2):x+w]
                left_face_gray = gray[y:y+h, x+int(w/2):x+w]

                right_face = frame[y:y+h, x:x+int(w/2)]
                right_face_gray = gray[y:y+h, x:x+int(w/2)]

                # Detect the left eye
                left_eye = left_eye_detector.detectMultiScale(
                    left_face_gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags = cv2.CASCADE_SCALE_IMAGE
                )

                # Detect the right eye
                right_eye = right_eye_detector.detectMultiScale(
                    right_face_gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags = cv2.CASCADE_SCALE_IMAGE
                )

                eye_status = '1' # we suppose the eyes are open

                # For each eye check wether the eye is closed.
                # If one is closed we conclude the eyes are closed
                for (ex,ey,ew,eh) in right_eye:
                    color = (0,255,0)
                    pred = predict(right_face[ey:ey+eh,ex:ex+ew], model)
                    if pred == 'closed':
                        eye_status='0'
                        color = (0,0,255)
                    cv2.rectangle(right_face,(ex,ey),(ex+ew,ey+eh),color,2)
                for (ex,ey,ew,eh) in left_eye:
                    color = (0,255,0)
                    pred = predict(left_face[ey:ey+eh,ex:ex+ew], model)
                    if pred == 'closed':
                        eye_status='0'
                        color = (0,0,255)
                    cv2.rectangle(left_face,(ex,ey),(ex+ew,ey+eh),color,2)
                eyes_detected[name] += eye_status

            if isBlinking(eyes_detected[name],3):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                # Display name
                y = y - 15 if y - 15 > 15 else y + 15
                cv2.putText(frame, 'Real', (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
                print("Real")
                say(l6)
                terminate(video_capture)
                break
                # eyes_detected[name] = '111'
            else:
                if len(eyes_detected[name]) > 20:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    # Display name
                    y = y - 15 if y - 15 > 15 else y + 15
                    cv2.putText(frame, 'Fake', (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 0, 255), 2)
                    print("Fake")
                    say(l7)
                    terminate(video_capture)
                    break
                break
            break


        return frame

def go(cap):
    
    #print("Spoof detector initialized")
    say(l4)
    say(l5)
    
    (model, face_detector, open_eyes_detector, left_eye_detector, right_eye_detector, images) = init()
    
    #data = process_and_encode(images)
    data = np.load('encodings.npy',allow_pickle='TRUE').item()
    #print(known_names)
    
    #video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    video_capture = cap
    #VideoStream(src=0).start()
    
    eyes_detected = defaultdict(str)
    while cap.isOpened():
      frame = detect_and_display(model, video_capture, face_detector, open_eyes_detector,left_eye_detector,right_eye_detector, data, eyes_detected)
      
      display(frame, cap)
      #cv2.imshow("Eye-Blink based Liveness Detection for Facial Recognition", frame)
      #if cv2.waitKey(1) & 0xFF == ord('q'):
      #    break
    #cv2.destroyAllWindows()
    #video_capture.release()
    #stop()
    
def display(img, cap):
    cv2.imshow("cam modules", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        
def terminate(cap):
    cv2.destroyAllWindows()
    cap.release()
        
init_cam()