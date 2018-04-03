import socket
import subprocess

#to be used in hub.py
def advertiseHubIP():
    thisIP = subprocess.check_output(["hostname", "-I"]).split()[0]
    thisIP = str(thisIP)#[2:-1]
    UDP_PORT = 5005
    for i in range(1,255):
        UDP_IP = "192.168.1." + str(i)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto("RatTrapHub: " + thisIP, (UDP_IP, UDP_PORT))

#to be used in trap.py
def getHubIP():
    IP = subprocess.check_output(["hostname", "-I"]).split()[0]
    UDP_IP = str(IP)#[2:-1]
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        if data.split()[0] == "RatTrapHub:":
            return data.split()[1]