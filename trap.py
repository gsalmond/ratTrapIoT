# Code to be run continously on a individual trap

import socket
import subprocess

# sends individual packets out over a local network to potential rat traps containing ip of hub
def advertiseHubIP():
    thisIP = subprocess.check_output(["hostname", "-I"]).split()[0]
    thisIP = str(thisIP)#[2:-1]
    UDP_PORT = 5005
    for i in range(1,255):
        UDP_IP = "192.168.1." + str(i)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto("RatTrapHub: " + thisIP, (UDP_IP, UDP_PORT))