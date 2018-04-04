import socket
import subprocess
import RPi.GPIO as GPIO
import time
import threading
from threading import Thread
from TrapClass import TrapClass

serverIP = None

# to be run when a rat trap is not associated with a hub, returns hub ip address as a string
def getHubIP():
    IP = subprocess.check_output(["hostname", "-I"]).split()[0]
    UDP_IP = str(IP)
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        print('Waiting to be discovered...')
        data, addr = sock.recvfrom(1024)
        if data.split()[0] == "RatTrapHub:":
            print('found hub')
            return data.split()[1]
        
def missedSwitch(channel):
    global t
    #print("missed flag", t.getMissedFlag())
    if GPIO.input(4):
        GPIO.output(9, GPIO.HIGH)
        print ("red light on")
        #if t.getMissedFlag() is not True:
        t.setMissedFlag(True)
    else:
        GPIO.output(9, GPIO.LOW)
        print ("red light off")
        #if t.getMissedFlag() is not False:
        t.setMissedFlag(False)
        

def setSwitch(channel):
    global t
    #print("set flag", t.getSetFlag())
    if GPIO.input(13):
        GPIO.output(10, GPIO.HIGH)
        print ("green light on")
        #if t.getSetFlag() is not True:
        t.setSetFlag(True)
    else:
        GPIO.output(10, GPIO.LOW)
        print ("green light off")
        #if t.getSetFlag is not False:
        t.setSetFlag(False)

hubIP = getHubIP()
t = TrapClass(123, "Rat", hubIP, 9050)
t.setInitialState()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #input for trap start state / missed state
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # input for trap set state
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

GPIO.add_event_detect(4, GPIO.BOTH)
GPIO.add_event_detect(13, GPIO.BOTH)
GPIO.add_event_callback(4, missedSwitch)
GPIO.add_event_callback(13, setSwitch)

try:
 while True:
  time.sleep(1)
finally:
 GPIO.cleanup()
