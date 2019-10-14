# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

DIGITALIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIGITALIN, GPIO.IN)
GPIO.setwarnings(False)

value = GPIO.digitalRead(DIGITALIN)
print DIGITALIN
