import subprocess
import requests
import re
from time import sleep

# This lab has you ping a specific IP Address to find it’s MAC Address and then shows you it’s vendor.

command = 'arp -a'
response = subprocess.check_output(command , shell=True)
#print(response)

response = str(response).split('\\n?')

for line in response:
    ip_text = ''
    mac_text = ''
    vendor_text = ''
    ip = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
    if ip:
        ip_text = ip.group()
        ip_text = ip_text.replace('(', '')
        ip_text = ip_text.replace(')', '')
    
    mac = re.search(r'([0-9A-Fa-f]{1,2}[:-]){5}[0-9A-Fa-f]{1,2}', line)
    if mac:
        mac_text = mac.group()
        url = f'https://www.macvendorlookup.com/api/v2/{mac_text}'
        try:
            vendor = requests.get(url).json()
            vendor_text = vendor[0]['company']
        except:
            pass

    print(f'Record:\t{ip_text}\t{mac_text}\t{vendor_text}')

    sleep(2)