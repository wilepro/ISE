import requests
from requests.auth import HTTPBasicAuth
from rich import print
import urllib3

urllib3.disable_warnings()

ISE_IP = "10.10.20.77"
USERNAME = "admin"
PASSWORD = "QAWSedrf1234!"

ancendpoint_url = f"https://{ISE_IP}/ers/config/ancendpoint/7f71296e-2900-492c-84f9-f1dda532fb68"
headers = {
    "Accept": "application/json"
}


response = requests.get(
    url=ancendpoint_url, 
    headers=headers, 
    auth=HTTPBasicAuth(USERNAME, PASSWORD), 
    verify=False
)

print(response.status_code)
print(response.text)
