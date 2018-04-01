import socket
import subprocess

IP = subprocess.check_output(["hostname", "-I"]).split()[0]
UDP_IP = str(IP)[2:-1]
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Host IP: " + UDP_IP)

while True:
	data, addr = sock.recvfrom(1024)
	print "recieved message:", data