#!/usr/bin/env bash
sudo bash -c "/usr/bin/mongod --config /blog-api/data/mongod.conf > /blog-api/logs/db_logs.txt 2>&1 &"
sudo bash -c "python3 /blog-api/index.py > /blog-api/logs/app_logs.txt 2>&1 &"