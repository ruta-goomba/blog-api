#!/usr/bin/env bash
cd /blog-api
pip3 install -r requirements.txt
cd /blog-api/nn_models
mkdir bottleneck_features
cd bottleneck_features
wget https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogResnet50Data.npz