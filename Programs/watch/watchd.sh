#!/bin/bash --rcfile

source /etc/bash.bashrc
source ~/.bashrc
source ~/env/bin/activate

export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/vision.json
echo $GOOGLE_APPLICATION_CREDENTIALS
#amixer --card 1 cset numid=11 100%

cd /home/pi/Programs/watch
echo "Running button_watch.py!"
python button_watch.py
echo "Watch Program is done!"


