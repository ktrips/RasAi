#!/bin/bash --rcfile

source /etc/bash.bashrc
source ~/.bashrc

export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/vision.json
echo $GOOGLE_APPLICATION_CREDENTIALS
#amixer --card 1 cset numid=11 100%

cd /home/RasAi/Programs
echo "Running button_vision.py!"
python button_vision.py
echo "Vision is done!"
