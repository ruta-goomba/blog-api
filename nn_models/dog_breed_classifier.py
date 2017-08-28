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

if os.environ.get("ENV"):
  bottleneck_features = '/Users/rutasakalauskaite/Documents/blog-api/nn_models/bottleneck_features/DogResnet50Data.npz'
  model_weights = '/Users/rutasakalauskaite/Documents/blog-api/nn_models/saved_models/weights.best.Resnet50.hdf5'
  dog_image_json = '/Users/rutasakalauskaite/Documents/blog-api/data/files/dog_images.json'
else:
  bottleneck_features = '/blog-api/nn_models/bottleneck_features/DogResnet50Data.npz'
  model_weights = '/blog-api/nn_models/saved_models/weights.best.Resnet50.hdf5'
  dog_image_json = '/blog-api/data/files/dog_images.json'

# # define function to load datasets
# def load_dataset(path):
#     data = load_files(path)
#     dog_files = np.array(data['filenames'])
#     dog_targets = np_utils.to_categorical(np.array(data['target']), 133)
#     return dog_files, dog_targets
#
# # load test datasets
# test_files, test_targets = load_dataset('../data/files/dog_images')

bottleneck_features = np.load(bottleneck_features)
train_Resnet50 = bottleneck_features['train']
valid_Resnet50 = bottleneck_features['valid']
test_Resnet50 = bottleneck_features['test']


Resnet50_model = Sequential()
Resnet50_model.add(GlobalAveragePooling2D(input_shape=train_Resnet50.shape[1:]))
Resnet50_model.add(Dense(133, activation='softmax'))

# Resnet50_model.summary()

# Compile the model.
Resnet50_model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# Train the model.
# checkpointer = ModelCheckpoint(filepath='saved_models/weights.best.Resnet50.hdf5',
#                                verbose=1, save_best_only=True)
#
# Resnet50_model.fit(train_Resnet50, train_targets,
#           validation_data=(valid_Resnet50, valid_targets),
#           epochs=20, batch_size=20, callbacks=[checkpointer], verbose=1)

# Load the model weights with the best validation loss.
Resnet50_model.load_weights(model_weights)


# Calculate classification accuracy on the test dataset.
# get index of predicted dog breed for each image in test set
# Resnet50_predictions = [np.argmax(Resnet50_model.predict(np.expand_dims(feature, axis=0))) for feature in test_Resnet50]
#
# # report test accuracy
# test_accuracy = 100*np.sum(np.array(Resnet50_predictions)==np.argmax(test_targets, axis=1))/len(Resnet50_predictions)
# print('Test accuracy: %.4f%%' % test_accuracy)


# load list of dog names
def get_dog_names():
  dog_names = []
  with open(dog_image_json) as data_file:
    data = json.load(data_file)
  for entry in data:
    directory, fileName = entry.split('/')
    numb, name = directory.split('.')
    name = name.replace('_', ' ')
    dog_names.append(name)
  return list(sorted(set(dog_names)))

dog_names = get_dog_names()

def Resnet_predict_breed(img_path):
    # extract bottleneck features
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    # obtain predicted vector
    predicted_vector = Resnet50_model.predict(bottleneck_feature)
    # return dog breed that is predicted by the model
    return dog_names[np.argmax(predicted_vector)]
