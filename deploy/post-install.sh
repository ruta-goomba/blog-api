#!/usr/bin/env bash
cd /blog-api/data
sudo mkdir db
sudo chmod 777 -R db
cd /blog-api
mkdir bottleneck_features
cd bottleneck_features
wget https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogResnet50Data.npz
sudo service nginx restart