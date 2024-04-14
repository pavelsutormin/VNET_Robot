import os
import subprocess
import time

try:
    os.system("sudo nmcli connection up VNET")
    server = subprocess.Popen("sudo python3 server.py".split(" "))
    #RUN SERVER:
    #server = subprocess.Popen("python3 -m http.server -b <IP> <PORT>".split(" "), cwd="<DIR>")
    print("Servers are up!")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
try:
    server.terminate()
    print("Servers are down!")
except Exception as e:
    print(e)
os.system("sudo nmcli connection down VNET")
