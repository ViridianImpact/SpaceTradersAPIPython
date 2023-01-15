#B0undle55
#Planets_Check.py
#Sends a GET request to the URL https://api.spacetraders.io/systems/OE/locations to view the planets in the OE region
#
#
#

import requests
from Logging_Script import log_response

"""
token; my personal token for authentication
choice; the loan type of the loan requested
"""
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
choice = 'PLANET'

#the URL related to areas within the OE system
url = 'https://api.spacetraders.io/systems/OE/locations'

#header contents
headers = {
    'Authorization': 'Bearer ' + token
    }

#data contents
data = {
    'type': choice
    }

#sending a get request and recording the response payload to the variable response
response = requests.get(url, headers=headers, params=data)

print(response.text)

#if the status code is good print the payload to console and record the system log, otherwise, print the error and record the error log
if response.status_code == 200:
    print(response.json())
    log_response(response, 'System_Log.txt')
else:
    print('Error:', response.status_code, response.reason)
    log_response(response, 'error_log.txt')




