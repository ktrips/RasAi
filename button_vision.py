#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import subprocess

from pixels import pixels

BUTTON = 17
hold_time=1.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

actions = ['python vision.py --detect face', #ボタン長押しで笑顔検出
           'python vision.py --detect label', #ワンプッシュでラベル読み取り
           'python vision.py --detect text']
pixels.wakeup()
time.sleep(hold_time)
pixels.off()

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

      pixels.think()
      print count

      cmd = actions[count]
      print cmd
      if cmd:
        subprocess.call(actions[count], shell=True)

      GPIO.remove_event_detect(BUTTON)
      GPIO.add_event_detect(BUTTON, GPIO.FALLING)
      pixels.off()
