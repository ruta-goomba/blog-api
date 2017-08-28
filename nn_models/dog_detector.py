from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image
from tqdm import tqdm
import numpy as np
import requests
from io import BytesIO

# define ResNet50 model
ResNet50_model = ResNet50(weights='imagenet')

def path_to_tensor(img_path):
    response = requests.get(img_path)
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(BytesIO(response.content), target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)

def ResNet50_predict_labels(img_path):
    # returns prediction vector for image located at img_path
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

# when looking at https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a
# you will notice that the categories corresponding to dogs appear in an uninterrupted sequence and
# correspond to dictionary keys 151-268, inclusive, to include all categories from 'Chihuahua' to 'Mexican hairless'.
# Thus, in order to check to see if an image is predicted to contain a dog by the pre-trained ResNet-50 model, we need
# only check if the ResNet50_predict_labels function above returns a value between 151 and 268 (inclusive).
# returns "True" if a dog is detected in the image stored at img_path
def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))