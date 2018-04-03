import socket
import subprocess
import threading
from threading import Thread
from senseOutput import SenseOutput
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

o = SenseOutput('Duncan')

# sends individual packets out over a local network to potential rat traps containing ip of hub
def advertiseHubIP():
    print ("advertise")
    thisIP = subprocess.check_output(["hostname", "-I"]).split()[0]
    thisIP = str(thisIP)#[2:-1]
    UDP_PORT = 5005
    for i in range(1,255):
        UDP_IP = "192.168.1." + str(i)
        print (UDP_IP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto("RatTrapHub: " + thisIP, (UDP_IP, UDP_PORT))

def startServer():
    #setup socket
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #get IP address
    IP = subprocess.check_output(["hostname", "-I"]).split()[0]
    myIP = str(IP)

    #configure socket
    sock1.bind((myIP, 9050))
    sock1.listen(1) #allow only 1 connection
    connection, client_address = sock1.accept()

    try:
        while True:
            data = connection.recv(1024)
            status = str(data)
            if status == "caught":
                print (data)
                o.displayRat(1000)
                connection.sendall(data)# sends back the data 
            elif status == "missed":
                print (data)
                o.displayNoRat(1000)
                connection.sendall(data)# sends back the data
            elif status == "set":
                print (data)
                o.displayTick(1000)
                connection.sendall(data)# sends back the data 
            elif status == "unknown":
                print (data)
                o.displayCross(1000)
                connection.sendall(data)# sends back the data 
            elif status == "close":
                break
            else:
                pass
            
    finally:
        print ("closing server socket")
        #connection cleanup
        connection.close()
        
        
        
def discovery():
    global o
    loop = True
    while loop:
        #gets joystic events
        for event in o.accessSense().stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'middle':
                    #start sdvising IP and display search
                    print("discovery requested")
                    thread1 = Thread(target=o.displaySearch)
                    thread2 = Thread(target=advertiseHubIP)
                    thread1.start()
                    thread2.start()
                elif event.direction == 'up':
                    print('exit discovery')
                    loop = False
                    break
        
#create threads
serverThread = Thread(target=startServer)
discoveryThread = Thread(target=discovery)


serverThread.start()
discoveryThread.start()


#for x in traps:
 #   print (x)
