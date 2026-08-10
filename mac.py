import requests

# Print out the vendor of the MAC address.

mac_text = '00:0A:95:9D:68:16'  

url = f'https://www.macvendorlookup.com/api/v2/{mac_text}'

vendor = requests.get(url).json()
vendor_text = vendor[0]['company']

print(vendor_text)