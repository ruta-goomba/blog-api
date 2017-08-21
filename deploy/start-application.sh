#!/usr/bin/env bash
cd /blog-api
sudo bash -c "mongod --dbpath=/blog-api/data/db > db_logs.txt 2>&1 &"
sudo bash -c "python3 index.py > app_logs.txt 2>&1 &"