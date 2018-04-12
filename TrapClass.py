import RPi.GPIO as GPIO
import time
import socket

class TrapClass:
    #class variables

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #instance variables
    def __init__(self, tID, tType, IP, port):
        self.id = tID   #the trap ID
        self.type = tType   #the type of trap (Rat, Mouse, Stoat)
        self.trapState = 'missed'
        self.missed = True
        self.set = False
        self.serverIP = IP
        self.serverPort = port
        self.hasServerIP = True
    
    #connects to the server
    def connectToServer(self):
        print("connecting to server...")
        self.sock.connect((self.serverIP, self.serverPort)) #connect to server
        
    #sends current state to the hub
    def communicateStateSockets(self):
        print("communicating state...")
        
        print("sending state: ", self.trapState) 
        self.sock.sendall(self.trapState)
        time.sleep(2)
        reply = self.sock.recv(1024)
        print reply
        if (reply != "caught") or (reply != "missed") or (reply != "set") or (reply != "new") or (reply != "unknown"):
            self.hasServerIP = False

    #determines if there is an IP address set
    def hasHubIP(self):
        return self.hasServerIP
    
    #starts communicating with the hub
    def setInitialState(self):
        print("hubIP:", self.serverIP)
        print("hubPort:", self.serverPort)
        print("Setting inital state...")
        self.connectToServer()
        print("connected to server...")
        
    #updates the state of the set flag
    def setSetFlag(self, state):
        self.set = state
        self.setTrapState()
        
    #updates the state of the missed flag 
    def setMissedFlag(self, state):
        self.missed = state
        self.setTrapState()
    
    #gets the current state of the set flag
    def getSetFlag(self):
        return self.set
        
    #gets the current state of the missed flag
    def getMissedFlag(self):
        return self.missed
        
    #determines if the trap is set, missed (a rat) or caught (a rat) based on the state of the two flags (set, and missed)
    def setTrapState(self):
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
        self.communicateStateSockets()
  
