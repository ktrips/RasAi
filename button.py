import RPi.GPIO as GPIO
import time
from pixels import pixels

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

while True:
    state = GPIO.input(BUTTON)
    if state:
        print("off")
        pixels.off()
    else:
        print("on")
        pixels.wakeup()
    time.sleep(1)
