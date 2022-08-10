import requests
import sys
import json

# From https://github.com/bigevilbeard/Interface_Up_Restconf/blob/master/xe_int_up.py

# HOST = 'ios-xe-mgmt-latest.cisco.com'
HOST = 'ios-xe-mgmt.cisco.com'
PORT = 9443
USER = 'developer'
# USER = 'root'
PASS = 'C1sco12345'
# PASS = 'D_Vay!_10&'

requests.packages.urllib3.disable_warnings()


def main():
    # payload = '{"ietf-interfaces:interface": {"name": "GigabitEthernet2", "description": "Configured by RESTCONF", "type": "iana-if-type:ethernetCsmacd", "enabled": enable}}'
    payload = '{"ietf-interfaces:interface": {"name": "GigabitEthernet2", "description": "Configured by RESTCONF", "type": "iana-if-type:ethernetCsmacd", "enabled": false}}'

    url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    }
    response = requests.put(url, auth=(USER, PASS), headers=headers, verify=False, data=payload)

    print(response.text)

    url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    }
    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False, data=payload)

    jsonResponse = response.json()
    for i in jsonResponse.items():
        print(f'Interface Name: {jsonResponse["ietf-interfaces:interface"]["name"]}')
        print(f'Interface Description: {jsonResponse["ietf-interfaces:interface"]["description"]}')
        print(f'Interface Status: {jsonResponse["ietf-interfaces:interface"]["enabled"]}')


if __name__ == '__main__':
    sys.exit(main())