import numpy as np
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dropout, Flatten, Dense
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
from sklearn.datasets import load_files
from keras.utils import np_utils
from nn_models.extract_bottleneck_features import extract_Resnet50
from nn_models.dog_detector import path_to_tensor
from skimage import io
from glob import glob
import json
import os

Resnet50_model = Sequential()
Resnet50_model.add(GlobalAveragePooling2D(input_shape=(1, 1, 2048)))
Resnet50_model.add(Dense(133, activation='softmax'))

Resnet50_model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

Resnet50_model.load_weights(os.path.join(os.path.dirname(__file__), 'saved_models/weights.best.Resnet50.hdf5'))

# load list of dog names
def get_dog_names():
  dog_names = []
  with open(os.path.join(os.path.dirname(__file__), '../data/files/dog_images.json')) as data_file:
    data = json.load(data_file)
  for entry in data:
    directory, fileName = entry.split('/')
    numb, name = directory.split('.')
    name = name.replace('_', ' ')
    dog_names.append(name)
  return list(sorted(set(dog_names)))

def Resnet_predict_breed(img_path):
    # extract bottleneck features
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    # obtain predicted vector
    predicted_vector = Resnet50_model.predict(bottleneck_feature)
    # return dog breed that is predicted by the model
    dog_names = get_dog_names()
    return dog_names[np.argmax(predicted_vector)]