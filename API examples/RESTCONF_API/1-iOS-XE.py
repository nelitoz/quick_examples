import requests

# Script from Postman

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-yang-library:modules-state"

payload={}
headers = {
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

