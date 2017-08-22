#!/usr/bin/env bash
cd /blog-api/data
sudo mkdir db
sudo chmod 777 -R db
sudo service nginx restart