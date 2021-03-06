# The Internet Assigned Numbers Authority (IANA) reserves the following IP address blocks for use as private IP addresses:
# 10.0.0.0 to 10.255.255.255.
# 172.16.0.0 to 172.31.255.255.
# 192.168.0.0 to 192.168.255.255.

import socket
import subprocess

thisIP = subprocess.check_output(["hostname", "-I"]).split()[0]
thisIP = str(thisIP)#[2:-1]

#UDP_IP = "127.0.0.1"
UDP_IP = "192.168.1.5"
UDP_PORT = 5005

for i in range(1,255):
   #print "UDP target IP:", UDP_IP
   #print "UDP target port:", UDP_PORT
   #print "message:", MESSAGE
   UDP_IP = "192.168.1." + str(i)
   MESSAGE = "sending to: " + UDP_IP
   print(MESSAGE)

   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.sendto(MESSAGE + " FROM: " + thisIP, (UDP_IP, UDP_PORT))