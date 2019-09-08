import RPi.GPIO as GPIO
import time

BUTTON = 26
LED = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)

while True:
    state = GPIO.input(BUTTON)
    if state:
        print("on")
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED, GPIO.HIGH)
    else:
        print("off")
    time.sleep(1)
