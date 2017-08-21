#!/usr/bin/env bash
cd /blog-api
mongod --dbpath=/blog-api/data/db > db_logs.txt 2>&1 &
python index.py > app_logs.txt 2>&1 &