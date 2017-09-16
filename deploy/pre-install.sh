#!/usr/bin/env bash
if [ -d /blog-api ]; then
    sudo rm -rf /blog-api
fi

if ! [ -d /home/ubuntu/db ]; then
  cd /home/ubuntu && sudo mkdir db && sudo chmod 777 -R db
fi

sudo apt-get -y update
sudo apt-get -y install python3-pip python3-dev
sudo locale-gen en_GB.UTF-8
sudo apt-get -y install nginx
sudo apt-get -y install nginx-extras
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/nginx.conf

if ! [ -x "$(service mongod status)" ]; then
 sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
 echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
 sudo apt-get update
 sudo apt-get install -y mongodb-org
fi

cd /
sudo mkdir blog-api
cd /blog-api