#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import sys
import argparse
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
 
class mdriver:
    def __init__(self, pwm, in1, in2):
         # GPIO setup
         #GPIO.setmode(GPIO.BCM)
         GPIO.setup(pwm, GPIO.OUT)
         GPIO.setup(in1, GPIO.OUT)
         GPIO.setup(in2, GPIO.OUT)
         # Pin setup
         self.in1 = in1
         self.in2 = in2
         self.p = GPIO.PWM(pwm, 50)

    def drive(self, speed):
         if speed > 0:
                GPIO.output(self.in1, 1)
                GPIO.output(self.in2, 0)
                self.p.start(speed)
         if speed < 0:
                GPIO.output(self.in1, 0)
                GPIO.output(self.in2, 1)
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
 
def main(direction, speed, duration):
    d1 = mdriver(22, 13, 19)
    d2 = mdriver(27, 5, 6)

    print('Move %s %s speed %s seconds' % (direction, speed, duration))
    speed   =int(speed)
    duration=int(duration)
    if direction == "f":
        d1.drive(speed)
        d2.drive(speed)
    elif direction == "r":
        d1.drive(-speed)
        d2.drive(speed)
    elif direction == "l":
        d1.drive(speed)
        d2.drive(-speed)
    elif direction == "b":
        d1.drive(-speed)
        d2.drive(-speed)
    time.sleep(duration)
    d1.brake()
    d2.brake()
    GPIO.cleanup()
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('direction', nargs='?', default="f", help='Direction of the movement: f, r, l, b')
    parser.add_argument('speed', nargs='?', default="100", help='Speed from -100 to 100')
    parser.add_argument('duration', nargs='?', default="1", help='Duration of motor time')
    args = parser.parse_args()
    result = main(args.direction, args.speed, args.duration)
