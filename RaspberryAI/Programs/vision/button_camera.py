#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import subprocess

BUTTON = 20
LED    = 16
hold_time=1.5
detect_camera = "/home/pi/Programs/vision/detect_camera.py"

import os
dir_aquest    = "/home/pi/Programs/aquestalkpi/"
CARD  = 0
DEVICE= 0
VOLUME= 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setwarnings(False)

for i in range(3):
      GPIO.output(LED, GPIO.HIGH)
      time.sleep(0.5)
      GPIO.output(LED, GPIO.LOW)
      time.sleep(0.5)

text = "シャッターを一回押すと物体判別、二回連続で押すと文字識別、長押しで笑顔判定を行います！"
os.system(dir_aquest + 'AquesTalkPi -g {} {} | aplay -D plughw:{},{}'.format(VOLUME, text, CARD, DEVICE))

actions = ['python ' + detect_camera + ' faces camera', #長押しで顔検出
           'python ' + detect_camera + ' labels camera', #ワンプッシュで物体判定
           'python ' + detect_camera + ' text camera'] #ダブルプッシュで文字検出

GPIO.add_event_detect(BUTTON,GPIO.FALLING)

while True:
    time.sleep(0.2)
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)
    if GPIO.event_detected(BUTTON):
      GPIO.remove_event_detect(BUTTON)
      now = time.time()
      count = 0
      GPIO.add_event_detect(BUTTON,GPIO.RISING)
      while time.time() < now + hold_time:
        if GPIO.event_detected(BUTTON):
          count +=1
          time.sleep(.3) # debounce time

      print(count)
      if count == 0:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(hold_time)
        GPIO.output(LED, GPIO.LOW)
      for i in range(count):
        time.sleep(0.5)
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED, GPIO.LOW)

      cmd = actions[count]
      print(cmd)
      if cmd:
        subprocess.call(actions[count], shell=True)

      GPIO.remove_event_detect(BUTTON)
      GPIO.add_event_detect(BUTTON, GPIO.FALLING)

