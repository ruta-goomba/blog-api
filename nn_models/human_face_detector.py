import cv2
from skimage import io
import os

if os.environ.get("ENV"):
  face_detect_model = '/Users/rutasakalauskaite/Documents/blog-api/nn_models/haarcascades/haarcascade_frontalface_alt.xml'
else:
  face_detect_model = '/blog-api/nn_models/haarcascades/haarcascade_frontalface_alt.xml'

# extract pre-trained face detector
face_cascade = cv2.CascadeClassifier(face_detect_model)

# returns "True" if face is detected in image stored at img_path
def face_detector(img_path):
    img = io.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0