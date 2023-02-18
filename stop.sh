#!/bin/bash
docker compose -f /home/pi/price_alarm/docker-compose.yml down

#Kill with SIGINT
kill -2 $(ps aux | grep '[p]ython3 /home/pi/price_alarm/server.py' | awk '{print $2}')
