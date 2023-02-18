#!/bin/bash

# start the mongo db database
docker compose up -f /home/pi/price_alarm/docker-compose.yml -d
# wait some until it starts
sleep 10
# start the server
source /home/pi/price_alarm/env/bin/activate
python3 -u /home/pi/price_alarm/server.py > /home/pi/price_alarm/out.log 2>&1 &