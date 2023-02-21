#!/bin/bash
docker container stop mongodb && docker container rm mongodb

#Kill with SIGINT
kill -2 $(ps aux | grep '[p]ython3 -u /home/pi/price_alarm/server.py' | awk '{print $2}')
