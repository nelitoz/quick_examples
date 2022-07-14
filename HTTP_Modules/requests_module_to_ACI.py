import requests
import json
requests.packages.urllib3.disable_warnings()


def login(apic, u, p):
    url = f"https://{apic}/api/aaaLogin.json?gui-token-request=yes"
    payload = {"aaaUser": {"attributes": {"name": u, "pwd": p}}}
    payload = "{\n\"aaaUser\":{\n\"attributes\":{\n\"name\":\"apic#LOCAL\\\\cisco\",\n\"pwd\":\"P1th0n2021!\"\n}\n}\n}"
    response = requests.request("POST", url, data=payload, verify=False)
    response_json = response.json()
    token = response_json['imdata'][0]["aaaLogin"]["attributes"]["urlToken"]
    cookies = response.cookies
    return token, cookies


def getBDs(apic, token, cookie, TENANT_NAME):
    tenant_dn = f"uni/tn-{TENANT_NAME}"
    url = f'https://{apic}/api/mo/{tenant_dn}.json?' \
          f'query-target=subtree&' \
          f'target-subtree-class=fvBD,fvCtx,fvRsCtx,fvAp&' \
          f'challenge={token}'
    response = requests.request("GET", url, verify=False, cookies=cookie)
    response_json = response.json()
    return response_json


t, c = login("172.27.76.11", "apic:LOCAL\\dacasti2", "?Superl0k13")
BDs = getBDs("172.27.76.11", t, c, "FIDUPREVISORA")
print(json.dumps(BDs, indent=2))