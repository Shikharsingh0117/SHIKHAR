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
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()
time.sleep(2)

print(yellow+b+ f' IP address is: {socket.gethostbyname(host_name)}')
os.system('git clone https://github.com/cyweb/hammer')
os.system('cd hammer')
os.system('python3 hammer.py')