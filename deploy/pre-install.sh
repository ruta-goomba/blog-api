#!/usr/bin/env bash
if [ -d /blog-api ]; then
    sudo rm -rf /blog-api
fi

sudo rm -rf /var/lib/apt/lists/*
sudo apt-get clean

sudo apt-get update
sudo apt-get -y install python3-pip python3-dev
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
pip3 install -U pytest
pip3 install -r requirements.txt
pip3 install flask
pip3 install -U flask-cors
sudo apt-get -y update
sudo apt-get -y install nginx
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/nginx.conf

cd /
sudo mkdir blog-api
cd /blog-api