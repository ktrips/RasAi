import RPi.GPIO as GPIO
import time
BUTTON = 16
LED = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
state = GPIO.input(BUTTON)
print(state)
GPIO.add_event_detect(BUTTON,GPIO.FALLING)

while True:
    state = GPIO.input(BUTTON)
    print(state)
    if GPIO.event_detected(BUTTON):
    #if state:
        print("off")
    else:
        print("ON")
        time.sleep(1)
    time.sleep(1)

