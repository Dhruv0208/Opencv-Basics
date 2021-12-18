import numpy as np
import cv2 as cv
import os

people = []
for i in os.listdir(r'A:\GitHub\opencv_practice\Faces\train'):
    people.append(i)

haar_cascade = cv.CascadeClassifier('Face_detection_using_haar_cascade\haar_cascade_face.xml')

features = np.load('Features.npy', allow_pickle=True)
labels = np.load('Labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'A:\GitHub\opencv_practice\Faces\val\elton_john\1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', img)

#detecting faces

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)

    print(f'Label = {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), thickness=1)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected person', img)
cv.waitKey(0)