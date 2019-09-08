#!/usr/bin/env python
import skywriter
import signal
import os

import wiringpi
import time
import sys

motor1_pin = 14
motor2_pin = 15

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( motor1_pin, 1 )
wiringpi.pinMode( motor2_pin, 1 )

second = 3

some_value = 5000

#@skywriter.move()
#def move(x, y, z):
#  print( x, y, z )

@skywriter.flick()
def flick(start,finish):
  print('Got a flick!', start, finish)
  wiringpi.pinMode( motor1_pin, 1 )
  wiringpi.pinMode( motor2_pin, 1 )
  if start == "north" and finish == "south":
      print('Go forward '+str(second))
      wiringpi.digitalWrite( motor1_pin, 1 )
      wiringpi.digitalWrite( motor2_pin, 0 )
      time.sleep(second)

  elif start == "south" and finish == "north":
      print('Back ward '+str(second))
      wiringpi.digitalWrite( motor1_pin, 0 )
      wiringpi.digitalWrite( motor2_pin, 1 )
      time.sleep(second)

  wiringpi.digitalWrite( motor1_pin, 1 )
  wiringpi.digitalWrite( motor2_pin, 1 )
  #time.sleep(second)
  wiringpi.pinMode( motor1_pin, 0 )
  wiringpi.pinMode( motor2_pin, 0 )

@skywriter.airwheel()
def spinny(delta):
  global some_value
  some_value += delta
  if some_value < 0:
  	some_value = 0
  if some_value > 10000:
    some_value = 10000
  print('Airwheel:', some_value/100)

@skywriter.double_tap()
def doubletap(position):
  print('Double tap!', position)
  os.system("python3 /home/pi/assistant-python-sdk/googlesamples/grpc/pushtotalk.py --once")

@skywriter.tap()
def tap(position):
  print('Tap!', position)

@skywriter.touch()
def touch(position):
  print('Touch!', position)

signal.pause()
