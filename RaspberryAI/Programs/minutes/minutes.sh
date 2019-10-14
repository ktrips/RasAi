#!/bin/bash --rcfile
source /home/pi/env/bin/activate
export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/RaspberryAi-0ebb5e021dba.json
echo $GOOGLE_APPLICATION_CREDENTIALS
cd /home/pi/Programs/minutes
echo "Streaming Minutes Device is running!"
python stream_minutes_device.py --repeat no --mail kenichi_yoshida@hotmail.com
echo "Streaming Minutes Device is completed!"