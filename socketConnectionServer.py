#Server Implementation
import socket
import subprocess
from senseOutput import SenseOutput

#setup output
o = SenseOutput("Duncan")

#setup socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get IP address
IP = subprocess.check_output(["hostname", "-I"]).split()[0]
myIP = str(IP)[2:-1]

#configure socket
sock.bind((myIP, 9050))
sock.listen(1) #allow only 1 connection
connection, client_address = sock.accept()

try:
    while True:
        data = connection.recv(128)
        status = str(data)[2:-1]
        if status == "caught":
            print (data)
            o.displayRat(1000)
            connection.sendall(data)# sends back the data probablly change this
        elif status == "miss":
            print (data)
            o.displayNoRat(1000)
            connection.sendall(data)# sends back the data probablly change this
        elif status == "set":
            print (data)
            o.displayTick(1000)
            connection.sendall(data)# sends back the data probablly change this
        else:
            break
        
finally:
    print ("Closing connection")
    #connection cleanup
    connection.close()
