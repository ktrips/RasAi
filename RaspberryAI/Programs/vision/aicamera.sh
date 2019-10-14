#!/bin/bash --rcfile
source /home/pi/env/bin/activate
export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/RaspberryAi-0ebb5e021dba.json
cd /home/pi/Programs/vision
echo "AI Camera is running!"
python button_camera.py
echo "AI Camera is done!"

