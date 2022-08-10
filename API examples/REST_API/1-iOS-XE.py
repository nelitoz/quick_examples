import requests

HOST = 'https://ios-xe-mgmt.cisco.com'
USER = "developer"
PASS = "C1sco12345"
PORT = 9443
headers = {'Accept': 'application/yang-data+xml',
            'Content-Type': 'application/yang-data+xml'
            }
URL = f"{HOST}:{PORT}/restconf/data/ietf-yang-library:modules-state"
response = requests.get(URL, auth=(USER, PASS), headers=headers, verify= False)
print(response.text)
print(response.status_code)
print(requests.codes.ok)