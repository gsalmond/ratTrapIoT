# Code to be run continously on a individual trap

import socket
import subprocess

from TrapClass import TrapClass

# to be run when a rat trap is not associated with a hub, returns hub ip address as a string
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

while True:
	hubIP = getHubIP()
	trapInstance = TrapClass(123, "Rat", hubIP, 9050)
	while trapInstance.hasHubIP():
		pass