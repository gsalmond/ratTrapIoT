import subprocess
from sense_hat import SenseHat

sense = SenseHat()

IP = subprocess.check_output(["hostname", "-I"]).split()[0]
#IP = subprocess.check_output(["hostname", "-I"])
print (str(IP))
#newIP = str(IP)
newIP = str(IP)[2:-1]
#myIP = newIP[2:-1:]
sense.show_message(newIP)


