#This lab has you ping a specific IP Address to find it’s MAC Address and then shows you it’s vendor.

import subprocess
import requests
import re

mac_text = 'Not Found'
vendor_text ='Not Found'

host = input('IP Address:')
print(f'IP Address: {host}')

try:
    command_ping = f'ping -c 1 {host}'
    response_ping = subprocess.check_output(command_ping, shell=True)
    #print(response_ping) #For Troubleshooting Purposes to Test Ping
    command = f'arp -a | grep -w {host}'
    response_arp = subprocess.check_output(command, shell=True)
    response_arp = str(response_arp)
    mac = re.search(r'([0-9A-Fa-f]{1,2}[:-]){5}[0-9A-Fa-f]{1,2}', response_arp)
    if mac:
        mac_text = mac.group()
    try:
        url = f'https://www.macvendorlookup.com/api/v2/{mac_text}'
        try:
            vendor = requests.get(url).json()
            vendor_text = vendor[0]['company']
        except:
            pass
    except:
        pass            
except:
    pass

print(f'MAC Address: {mac_text}')
print(f'Vendor: {vendor_text}')