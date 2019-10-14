# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

BUTTON = 20
LED    = 16
hold_time=1.5
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setwarnings(False)

for i in range(3):
      GPIO.output(LED, GPIO.HIGH)
      time.sleep(0.5)
      GPIO.output(LED, GPIO.LOW)
      time.sleep(0.5)

GPIO.add_event_detect(BUTTON,GPIO.FALLING)

while True:
     if GPIO.event_detected(BUTTON):
      GPIO.remove_event_detect(BUTTON)
      now = time.time()
      count = 0
      GPIO.add_event_detect(BUTTON,GPIO.RISING)
      while time.time() < now + hold_time:
        if GPIO.event_detected(BUTTON):
          count +=1
          time.sleep(.3) # debounce time

      print count
      if count == 0:
        GPIO.output(LED, GPIO.HIGH)
        os.system("aplay sound/0.wav") #time.sleep(hold_time)
        GPIO.output(LED, GPIO.LOW)
      for i in range(count):
        time.sleep(0.5)
        GPIO.output(LED, GPIO.HIGH)
        os.system("aplay sound/1.wav")
        #time.sleep(0.5)
        GPIO.output(LED, GPIO.LOW)

      GPIO.remove_event_detect(BUTTON)
      GPIO.add_event_detect(BUTTON, GPIO.FALLING)

