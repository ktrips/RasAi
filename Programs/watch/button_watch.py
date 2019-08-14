#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import subprocess

BUTTON   = 17
hold_time= 1.5
exec_dir = "/home/pi/Programs/watch/"

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
actions = ['python3 ' + exec_dir + 'assistant_once.py', #Google Assistant起動
           'python3 ' + exec_dir + 'stream_jp_watch.py', #ワンプッシュで日本語聞き取り開始
           'python3 ' + exec_dir + 'grove_oled_temp.py'] #ダブルプッシュで温湿度計測

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
      print(count)
      if count >= 2:
        count = 2
      cmd = actions[count]
      print(cmd)
      if cmd:
        subprocess.call(actions[count], shell=True)
      GPIO.remove_event_detect(BUTTON)
      GPIO.add_event_detect(BUTTON, GPIO.FALLING)

