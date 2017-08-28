import os
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import json
from nn_models.dog_detector import dog_detector
from nn_models.human_face_detector import face_detector
from nn_models.dog_breed_classifier import Resnet_predict_breed

if os.environ.get("ENV"):
  origins = 'http://localhost:3000'
  port=5001
else:
  origins = 'ec2-34-248-168-254.eu-west-1.compute.amazonaws.com'
  port=5000

app = Flask(__name__)
CORS(app)

@app.route("/dog_prediction", methods=['POST'])
def dog_prediction():
    if request.method == 'POST':
      data = json.loads(request.data)
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
    app.run(port=port)