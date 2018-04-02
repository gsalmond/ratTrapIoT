import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.OUT)

status = False

def onSwitch(channel):
 global status
 if status: 
  status = False
  GPIO.output(9, GPIO.LOW)
 else: 
  status = True
  GPIO.output(9, GPIO.HIGH)
  
 print("Channel %s went high" % channel)
 print("Current status is", status)



GPIO.add_event_detect(4, GPIO.RISING, callback=onSwitch, bouncetime=200)

try:
 while True:
  time.sleep(1)
finally:
 GPIO.cleanup()