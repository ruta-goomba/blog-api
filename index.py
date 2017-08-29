import os
from eve import Eve
from flask import request, jsonify
from flask_cors import CORS
import json
from nn_models.dog_detector import dog_detector
from nn_models.human_face_detector import face_detector
from nn_models.dog_breed_classifier import Resnet_predict_breed

if os.environ.get("ENV"):
  settings = 'settings_dev.py'
else:
  settings = 'settings_prod.py'

app = Eve(settings=settings)
CORS(app)

@app.route("/dog_prediction", methods=['POST'])
def dog_prediction():
    if request.method == 'POST':
      data = json.loads(str(request.data, 'utf8'))
      img_path = 'https://s3-eu-west-1.amazonaws.com/' + data['url']
      if(dog_detector(img_path)):
          pred = { "human": 0, "dog": 1, "breed": Resnet_predict_breed(img_path)}
      elif(face_detector(img_path)):
          pred = { "human": 1, "dog": 0, "breed": Resnet_predict_breed(img_path)}
      else:
          pred = { "human": 0, "dog": 0, "breed": ''}
      resp = jsonify(pred)
      resp.status_code = 200
      return resp

if __name__ == '__main__':
    app.run()
