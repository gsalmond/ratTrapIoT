import RPi.GPIO as GPIO
import time
import socket
import urllib

class TrapClass:
    #class variables

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    opener = urllib.FancyURLopener({})


    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #input for trap start state / missed state
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # input for trap set state
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)

    GPIO.add_event_detect(4, GPIO.BOTH)
    GPIO.add_event_detect(13, GPIO.BOTH)
    GPIO.add_event_callback(4, missedSwitch)
    GPIO.add_event_callback(13, setSwitch)

    #instance variables
    def __init__(self, tID, tType, IP, port):
        self.id = tID   #the trap ID
        self.type = tType   #the type of trap (Rat, Mouse, Stoat)
        self.trapState = 'new'
        self.missed = True
        self.set = False
        self.serverIP = IP
        self.serverPort = port

    def connectToServer(self):
        sock.connect(self.serverIP, self.serverPort) #connect to server

    def communicateStateSockets(self):
        sock.sendall(self.trapState)
        reply = s.recv(1024) #Review the size of this ?is it apprpriate
        print reply

    def communicateStateRoutes(self):
        if self.trapState == 'caught':
            print ("You need to implement the urllib properly")
        elif self.trapState == 'missed':
            print ("You need to implement the urllib properly")
        elif self.trapState == 'set':
            print ("You need to implement the urllib properly")
            f = opener.open('http://' + serverIP + ':5000/wait')
        elif self.trapState == 'unknown':
            print ("You need to implement the urllib properly")
        elif self.trapState == 'new':
            print ("You need to implement the urllib properly")

    def getTrapState(self):
        if self.missed == False and self.set == False:
            print ("You caught something")
            self.trapState = 'caught'
        elif self.missed == True and self.set == False:
            print ("The trap has been activated. It did not catch anything")
            self.trapState = 'missed'
        elif self.missed == False and self.set == True:
            print ("The trap has been set, and is being monitored for activity")
            self.trapState = 'set'
        else:
            print ("Error: Something is wrong with your trap. Please contact the developer")
            self.trapState = 'unknown'

    def missedSwitch(self, channel):
        if GPIO.input(4):
            GPIO.output(9, GPIO.HIGH)
            print ("red light on")
            print ("Missed the Rat")
            self.missed = True
        else:
            GPIO.output(9, GPIO.LOW)
            print ("red light off")
            self.missed = False

        #determine trapState
        self.getTrapState()

    def setSwitch(self, channel):
        if GPIO.input(13):
            GPIO.output(10, GPIO.HIGH)
            print ("green light on")
            print ("Trap is set")
            self.set = True
        else:
            GPIO.output(10, GPIO.LOW)
            print ("green light off")
            self.set = False

            #determine trapState
            self.getTrapState()
