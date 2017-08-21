#!/usr/bin/env bash
if [ -d /blog-api ]; then
    rm -rf /blog-api
fi

sudo rm -rf /var/lib/apt/lists/*
sudo apt-get clean

if ! [ -x "$(service mongod status)" ]; then
  sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
  echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
  sudo apt-get update
  sudo apt-get install -y mongodb-org
fi

pip3 install eve

cd /
sudo mkdir blog-api
cd /blog-api