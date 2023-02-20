#!/bin/bash

# start the mongo db database
docker compose -f /home/pi/price_alarm/docker-compose.yml up -d
# wait some until it starts
sleep 5
# start the server
source /home/pi/price_alarm/env/bin/activate
source /home/pi/price_alarm/.env
export EMAIL_USERNAME=$EMAIL_USERNAME
export EMAIL_PASSWORD=$EMAIL_PASSWORD
export FROM_EMAIL_ADDR=$FROM_EMAIL_ADDR
export ENV=$ENV
export SUB_DIRECTORY=$SUB_DIRECTORY
export DOMAIN=$DOMAIN
python3 -u /home/pi/price_alarm/server.py > /home/pi/price_alarm/out.log 2>&1 &