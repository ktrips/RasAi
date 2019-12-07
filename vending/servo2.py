import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

gp_out2 = 2
gp_out3 = 3
GPIO.setup(gp_out2, GPIO.OUT)
GPIO.setup(gp_out3, GPIO.OUT)
motor2 = GPIO.PWM(gp_out2, 50)
motor3 = GPIO.PWM(gp_out3, 50)
motor2.start(0.0)
motor3.start(0.0)

bot = 2.5
mid = 7.2
top = 12.0

#motor.ChangeDutyCycle(bot)
#time.sleep(0.5)

motor2.ChangeDutyCycle(bot)
motor3.ChangeDutyCycle(top)
time.sleep(2)

motor2.ChangeDutyCycle(mid)
motor3.ChangeDutyCycle(mid)
time.sleep(0.5)

GPIO.cleanup()
