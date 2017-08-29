#!/usr/bin/env bash
sudo bash -c "python3 /blog-api/index.py > /blog-api/logs/app_logs.txt 2>&1 &"
sudo service nginx restart