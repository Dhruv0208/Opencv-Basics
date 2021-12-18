# using opencv built in face recognizer

import os
import cv2 as cv
import numpy as np

people = []
train_dir = r'A:\GitHub\opencv_practice\Faces\train'
haar_cascade = cv.CascadeClassifier('Face_detection_using_haar_cascade\haar_cascade_face.xml')
for i in os.listdir(r'A:\GitHub\opencv_practice\Faces\train'):
    people.append(i)

features = []
labels = []
def train():
    for person in people:
        path = os.path.join(train_dir, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

train()
np.save('Features.npy', features)
np.save('Labels.npy', labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(np.array(features, dtype='object'), np.array(labels))
np.save('Features.npy', features)
np.save('Labels.npy', labels)
face_recognizer.save('face_trained.yml')