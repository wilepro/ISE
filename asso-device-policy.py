import requests
from requests.auth import HTTPBasicAuth
from rich import print
import urllib3

urllib3.disable_warnings()

ISE_IP = "10.10.20.77"
USERNAME = "admin"
PASSWORD = "QAWSedrf1234!"

MAC_ADDY = "AA:BB:CC:11:22:33"
POLICY_NAME = "NuggetPolicy"

ancendpoint_url = f"https://{ISE_IP}/ers/config/ancendpoint/apply"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "OperationAdditionalData": {
        "additionalData": [
            {"name": "macAddress", "value": MAC_ADDY},
            {"name": "policyName", "value": POLICY_NAME}
        ]
    }
}

response = requests.put(
    url=ancendpoint_url, 
    json=payload, 
    headers=headers, 
    auth=HTTPBasicAuth(USERNAME, PASSWORD), 
    verify=False
)

print(response.status_code)
print(response.text)
