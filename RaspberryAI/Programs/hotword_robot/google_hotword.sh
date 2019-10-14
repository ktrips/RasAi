#!/bin/bash --rcfile

source /etc/bash.bashrc
source /home/pi/.bashrc

source /home/pi/env/bin/activate
cd /home/pi/Programs/googlesamples/grpc/
echo "Google Assistant Button to Talk is running"
python buttontotalk.py
#googlesamples-assistant-hotword --credentials /home/pi/.config/google-oauthlib-tool/credentials.json --project-id raspberryai --device-model-id raspberryai-rasaiprd

echo "Google Assistant Button to Talk is done"

