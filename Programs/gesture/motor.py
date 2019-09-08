#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import sys
import argparse
import RPi.GPIO as GPIO

BUTTON = 26
LED    = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)

class ta7291:
        def __init__(self, pwm, in1, in2):
                # GPIO setup
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pwm, GPIO.OUT)
                GPIO.setup(in1, GPIO.OUT)
                GPIO.setup(in2, GPIO.OUT)
                # Pin setup
                self.in1 = in1
                self.in2 = in2
                self.p = GPIO.PWM(18, 50)
        def drive(self, speed):
                # speed: From -100 (Reverse) to 100 (Forward)
                if speed > 0:
                        GPIO.output(self.in1, 0)
                        GPIO.output(self.in2, 1)
                        self.p.start(speed)
                if speed < 0:
                        GPIO.output(self.in1, 1)
                        GPIO.output(self.in2, 0)
                        self.p.start(-speed)
                if speed == 0:
                        GPIO.output(self.in1, 0)
                        GPIO.output(self.in2, 0)
        def brake(self):
                GPIO.output(self.in1, 1)
                GPIO.output(self.in2, 1)
                time.sleep(0.5)
        def cleanup(self):
                self.brake()
                GPIO.cleanup()

def main(speed, duration):
        d = ta7291(18, 14, 15) #24, 25)
        print('Move %s speed %s seconds' % (speed, duration))
        GPIO.output(LED, GPIO.HIGH)
        speed   =int(speed)
        duration=int(duration)
        d.drive(speed)
        d.brake()
        GPIO.output(LED, GPIO.LOW)
        time.sleep(duration)
        d.cleanup()

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument('speed', nargs='?', default="100", help='Speed from -100 to 100')
        parser.add_argument('duration', nargs='?', default="1", help='Duration of motor time')
        args = parser.parse_args()
        result = main(args.speed, args.duration)
