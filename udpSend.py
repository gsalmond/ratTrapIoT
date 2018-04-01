# import socket

# #UDP_IP = "127.0.0.1"
# UDP_IP = "192.168.1.5"
# UDP_PORT = 5005
# MESSAGE = "My message is this"

# print "UDP target IP:", UDP_IP
# print "UDP target port:", UDP_PORT
# print "message:", MESSAGE

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

import socket

#UDP_IP = "127.0.0.1"
UDP_IP = "192.168.1.5"
UDP_PORT = 5005

for i in range(1,255):
   #print "UDP target IP:", UDP_IP
   #print "UDP target port:", UDP_PORT
   #print "message:", MESSAGE
   UDP_IP = "192.168.1." + str(i)
   MESSAGE = "ratTrapOn: " + UDP_IP
   print(MESSAGE)
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))