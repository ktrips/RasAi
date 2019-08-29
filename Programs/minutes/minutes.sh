#!/bin/bash --rcfile
source /home/pi/env/bin/activate
export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/RaspberryAi-0ebb5e021dba.json
echo $GOOGLE_APPLICATION_CREDENTIALS
cd /home/pi/Programs/minutes
echo "Auto Minutes is running!"
python stream_minutes.py
echo "Auto Minutes is completed!"
