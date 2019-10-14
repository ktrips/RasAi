import wiringpi as pi
import time

sw = 20

pi.wiringPiSetupGpio()
pi.pinMode(sw, pi.INPUT)

while True:
  if pi.digitalRead(sw) == pi.HIGH:
    print "ON"
  else:
    print "OFF"

  time.sleep(1)
