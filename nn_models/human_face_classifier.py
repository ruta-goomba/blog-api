import numpy as np
from glob import glob
from random import randint
import cv2
import matplotlib.pyplot as plt
import numpy as np
import urllib
from skimage import io
import json

# extract pre-trained face detector
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

# import the list of all image file urls
with open('../data/files/human_faces.json') as data_file:
    data = json.load(data_file)

# generate random image file index
index = randint(0, len(data));

# get image
img = io.imread('https://s3-eu-west-1.amazonaws.com/rg-human-faces/lfw/' + data[index])

#convert rgb image to bgr
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# convert BGR image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find faces in image
faces = face_cascade.detectMultiScale(gray)

# get bounding box for each detected face
for (x,y,w,h) in faces:
    # add bounding box to color image
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# convert BGR image to RGB for plotting
cv_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# display the image, along with bounding box
plt.imshow(cv_rgb)
plt.show()