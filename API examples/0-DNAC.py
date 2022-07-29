#Import required modules
import requests 
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

#Define constant information

SERVER="https://sandboxdnac.cisco.com"
AUTH_OBJ = '/dna/system/api/v1/auth/token'
NETWORK_HEALTH_OBJ = '/dna/intent/api/v1/network-health'

USERNAME = 'devnetuser'
PASSWORD = 'Cisco123!'

#Retrive the token
response = requests.post(SERVER + AUTH_OBJ, auth=HTTPBasicAuth(USERNAME, PASSWO
RD), verify=False)
token =response.json()['Token']


# make the API call request
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
response = requests.get(SERVER + NETWORK_HEALTH_OBJ, headers=headers, verify=Fa
lse)
network_health = response.json()['response']

# Parse and print data
print (f"\
    Good:{network_health[0]['goodCount']}, \
    BAD:{network_health[0]['badCount']}, \
    HealthScore: {network_health[0]['healthScore']}")


