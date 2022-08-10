# modules
import requests
import json

# parameters
url = "https://webexapis.com/v1/messages/"
token = "NTA0MjE3MDYtODhmYS00NThhLTkxYWItNjE3ZjQwMjQ5MmFkMmQwMDdjNmQtOWNl_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
roomid = "Y2lzY29zcGFyazovL3VzL1JPT00vMTlkNTdlYTAtNWY0Yi0xMWViLTgxYzAtYjcwZWY0ZDhkYWU3"
message = "hello from a python script again"

headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(token)}
data = {"roomId": "{}".format(roomid),
        "text": "{}".format(message)
        }

# request
request = requests.post(url, data=json.dumps(data), headers=headers, verify=True)

# results
print(request.status_code)
