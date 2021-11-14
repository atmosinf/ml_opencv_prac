import os
import cv2 as cv
import numpy as np

people = []
DIR = r'../resources/Faces/train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

for i in os.listdir(DIR):
    people.append(i)
# print(people)

features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person) # returns the index of the people list. eg: 0 is Seinfeld, 1 is Elton, etc

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # roi = region of interest
                features.append(faces_roi)
                labels.append(label) 

create_train()

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list
features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer.train(features, labels)

print('Training done------------------')
face_recognizer.save('face_trained.yaml')
np.save('features.npy', features)
np.save('labels.npy', labels)