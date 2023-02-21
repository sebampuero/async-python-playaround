#!/bin/bash

# start the mongo db database
if [ -z "$(docker ps -a -f "name=mongodb" -q )" ]; then
    docker run --name mongodb -p 27017:27017 -v /home/pi/price_alarm/mongo_volume:/data/db -d mongo:4.4.18
fi
if [ -n "$(docker ps -a -f "name=mongodb" -f "status=exited" -q )" ]; then
    docker container start mongodb
fi

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