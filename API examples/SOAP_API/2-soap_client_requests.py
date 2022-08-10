# import required modules
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

# Define relevant variables and static values
BASE_URL = "http://www.dneonline.com"
RESOURCE = "/calculator.asmx"
headers = {"Content-Type":"text/xml; charset=utf-8",}
payload = """\
<?xml version='1.0' encoding='utf-8'?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">\
 <soap-env:Body><ns0:Add xmlns:ns0="http://tempuri.org/"><ns0:intA>1</ns0:intA><ns0:intB>2</ns0:intB></ns0:Add></soap-env:Body>\
</soap-env:Envelope>
"""

#create the requests
response = requests.request("POST", url=BASE_URL+RESOURCE, verify=False, data=payload, headers=headers)

#print the requests
print (response)

print(response.text)
