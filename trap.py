import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

def onSwitch1(channel):
    if GPIO.input(4):
        GPIO.output(9, GPIO.HIGH)
        print ("red light on")
    else:
        GPIO.output(9, GPIO.LOW)
        print ("red light off")
        

def onSwitch2(channel):
    if GPIO.input(13):
        GPIO.output(10, GPIO.HIGH)
        print ("green light on")
    else:
        GPIO.output(10, GPIO.LOW)
        print ("green light off")

GPIO.add_event_detect(4, GPIO.BOTH)
GPIO.add_event_detect(13, GPIO.BOTH)
GPIO.add_event_callback(4, onSwitch1)
GPIO.add_event_callback(13, onSwitch2)

try:
 while True:
  time.sleep(1)
finally:
 GPIO.cleanup()
