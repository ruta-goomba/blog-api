#!/usr/bin/env bash
if [ -d /blog-api ]; then
    rm -rf /blog-api
fi

sudo rm -rf /var/lib/apt/lists/*
sudo apt-get clean

sudo apt-get update
sudo apt-get -y install python3-pip python3-dev
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
pip3 install -U pytest
pip3 install -r requirements.txt
pip3 install eve
pip3 install tensorflow
sudo pip3 install keras

if ! [ -x "$(service mongod status)" ]; then
  sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
  echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
  sudo apt-get update
  sudo apt-get install -y mongodb-org
fi

cd /
sudo mkdir blog-api
cd /blog-api