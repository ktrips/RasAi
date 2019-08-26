# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

BUTTON = 20
LED    = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
#GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BUTTON,GPIO.FALLING)

while True:
    if GPIO.event_detected(BUTTON):
        GPIO.output(LED, GPIO.HIGH)
        print "Switch ON!"
        time.sleep(0.5)
        GPIO.output(LED, GPIO.LOW)
    else:
        print "OFF"
    time.sleep(1)

GPIO.cleanup()	
