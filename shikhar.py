import time
import socket
import os
#colors
red='\033[91m'
b='\033[21m'
green='\033[92m'
yellow='\033[93m'
cyan='\033[96m'
blue='\033[94m'

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

print (red+b+"""
                    _
                   /_/-     .'''.
                =O(_))))...'    `.
                   \_\-    
                   
          
█▀ █░█ █ █▄▀ █░█ ▄▀█ █▀█   ▄▄
▄█ █▀█ █ █░█ █▀█ █▀█ █▀▄   ░░

"""+b+red)
host_name = input(green+b+"""

Enter the website address: """)

clearConsole()
time.sleep(2)

print(yellow+b+ f' IP address is: {socket.gethostbyname(host_name)}')
time.sleep(5)

clearConsole()

print(red+b+"""welcome in shikhar""")
time.sleep(1)
clearConsole()
print(green+b+"""start hacking.""")
time.sleep(1)
clearConsole()
print(green+b+"""start hacking..""")
time.sleep(1)
clearConsole()
print(green+b+"""start hacking...""")
time.sleep(1)
clearConsole()
print(green+b+"""start hacking....""")
time.sleep(1)
clearConsole()
print(green+b+"""start hacking.....""")
time.sleep(1)
clearConsole()
os.system('python3 slowloris.py host_name')