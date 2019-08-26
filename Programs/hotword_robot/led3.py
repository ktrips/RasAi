# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

LED1   = 16
LED2   = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

for i in range(3):
      GPIO.output(LED1, GPIO.HIGH)
      GPIO.output(LED2, GPIO.HIGH)
      time.sleep(0.5)
      print("LED ON!")
      GPIO.output(LED1, GPIO.LOW)
      GPIO.output(LED2, GPIO.LOW)
      time.sleep(0.5)
