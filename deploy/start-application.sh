#!/usr/bin/env bash
cd /blog-api/db
sudo bash -c "mongod --config mongod.conf > db_logs.txt 2>&1 &"
cd /blog-api
sudo bash -c "python3 index.py > app_logs.txt 2>&1 &"