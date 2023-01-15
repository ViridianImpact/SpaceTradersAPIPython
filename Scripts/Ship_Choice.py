#B0undle55
#Ship_Choice.py
#Sends a POST request to the URL https://api.spacetraders.io/my/ships to request a purchase of the specified ship
#
#
#

import requests
from Logging_Script import log_response

"""
token; my personal token for authentication
choice; the name of the ship to be purchased
location; the location selling the ship
"""
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
choice = 'JW-MK-I'
location = 'OE-PM-TR'

#the URL for making ship purchase requests
url = 'https://api.spacetraders.io/my/ships'

#header contents
headers = {
    'Authorization': 'Bearer ' + token
    }

#data contents
data = {
    'location': location,
    'type': choice
    }

#sending a post request and recording the response payload to the variable response
response = requests.post(url, json=data, headers=headers)

#if the status code is good print the payload to console and record the vehicle log, otherwise, print the error and record the error log
if response.status_code == 200:
    print(response.json())
    log_response(response, 'Vehicle_Log.txt')
else:
    print('Error:', response.status_code, response.reason)
    log_response(response, 'error_log.txt')

# token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
# user = 'ViridianImpact'
# shipID = 'clcwsbzgc107055215s63c83vr0d'

