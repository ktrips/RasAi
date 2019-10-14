# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import os

LED    = 16
BUTTON = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.add_event_detect(BUTTON,GPIO.FALLING)

hold_time = 1.5
sound_dir = "/home/pi/Programs/sound/"

while True:
    if GPIO.event_detected(BUTTON):
        GPIO.remove_event_detect(BUTTON)
        now = time.time()
        count = 0
        GPIO.add_event_detect(BUTTON,GPIO.RISING)
        while time.time() < now + hold_time:
            if GPIO.event_detected(BUTTON):
                count +=1
                time.sleep(.3)

        print count
        if count <> 0:					
            sound_file = "1"
        else:
            sound_file = "0"
        GPIO.output(LED, GPIO.HIGH)
        os.system("aplay " + sound_dir + sound_file + ".wav")
        GPIO.output(LED, GPIO.LOW)

        GPIO.remove_event_detect(BUTTON)
        GPIO.add_event_detect(BUTTON, GPIO.FALLING)

GPIO.cleanup(BUTTON)
