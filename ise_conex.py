import requests
from requests.auth import HTTPBasicAuth
from rich import print
import urllib3

urllib3.disable_warnings()

ISE_IP = "10.10.20.77"
USERNAME = "admin"
PASSWORD = "QAWSedrf1234!"

ancpolicy_url = f"https://{ISE_IP}/ers/config/ancpolicy"
headers = {
    "Content-Type": "application/json"
}

payload = {
    "ErsAncPolicy": {
        "name": "NuggetPolicy",
        "description": "Test Policy to Quarantine Devices",
        "actions": ["QUARANTINE"]
    }
}

response = requests.post(
    url=ancpolicy_url, 
    json=payload, 
    headers=headers, 
    auth=HTTPBasicAuth(USERNAME, PASSWORD), 
    verify=False
)

print(response.status_code)
print(response.text)
