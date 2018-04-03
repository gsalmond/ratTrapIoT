# Code to be run continously on a hub for rat traps

import socket
import subprocess
import treading
# from senseOutput import SenseOutput

#setup socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get IP address
# IP = subprocess.check_output(["hostname", "-I"]).split()[0]
# myIP = str(IP)[2:-1]

myIP = "127.0.0.1"

#configure socket
sock.bind((myIP, 9050))
sock.listen(1) #allow only 1 connection
connection, client_address = sock.accept()

def displayStatus():
    try:
        while True:
            data = connection.recv(128)
            status = str(data)[2:-1]
            if status == "caught":
                print (data)
                # o.displayRat(1000)
                connection.sendall(data)# sends back the data
            elif status == "missed":
                print (data)
                # o.displayNoRat(1000)
                connection.sendall(data)# sends back the data
            elif status == "set":
                print (data)
                # o.displayTick(1000)
                connection.sendall(data)# sends back the data
            elif status == "unknown":
                # o.displayCross(1000)
                connection.sendall(data) # sends back the data
            else:
                break

    finally:
        print ("Closing connection")
        #connection cleanup
        connection.close()

# sends individual packets out over a local network to potential rat traps containing ip of hub
def advertiseHubIP():
    thisIP = subprocess.check_output(["hostname", "-I"]).split()[0]
    thisIP = str(thisIP)#[2:-1]
    UDP_PORT = 5005
    for i in range(1,255):
        UDP_IP = "192.168.1." + str(i)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto("RatTrapHub: " + thisIP, (UDP_IP, UDP_PORT))

try:
    statusThread = threading.Thread(target=displayStatus)
    discoveryThread = threading.Thread(target=advertiseHubIP)
except:
    "Something went wrong with threads"
