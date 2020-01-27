mport RPi.GPIO as GPIO
from time import sleep

human_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(human_pin, GPIO.IN)

try:
    while True:
    print(GPIO.input(human_pin))
    sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
