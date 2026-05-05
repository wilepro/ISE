import requests
from requests.auth import HTTPBasicAuth
from rich import print
import urllib3

urllib3.disable_warnings()

ISE_IP = "10.10.20.77"
USERNAME = "admin"
PASSWORD = "QAWSedrf1234!"

endpoint_url = f"https://{ISE_IP}/ers/config/endpoint"
headers = {
    "Content-Type": "application/json"
}

payload = {
    "ERSEndPoint": {
        "name": "NUGGETENDPOINT",
        "description": "Test Endpoint for ENAUTO",
        "mac": "AA:BB:CC:11:22:33"
    }
}

response = requests.post(
    url=endpoint_url, 
    json=payload, 
    headers=headers, 
    auth=HTTPBasicAuth(USERNAME, PASSWORD), 
    verify=False
)

print(response.status_code)
print(response.text)
