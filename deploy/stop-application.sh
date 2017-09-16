#!/usr/bin/env bash
sudo service nginx stop
pkill -f index.py
sudo bash -c "sudo service mongod stop --config /blog-api/data/mongodb.conf"