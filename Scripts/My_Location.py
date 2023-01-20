#B0undle55
#My_Location.py
#Sends a GET request to the URL https://api.spacetraders.io/systems/OE/locations to view the planets in the OE region
#
#
#

import requests
from Logging_Script import log_response

def my_location(token):

    #the URL related to areas within the OE system
    url = 'https://api.spacetraders.io/my/ships'

    #header contents
    headers = {
        'Authorization': 'Bearer ' + token
        }

    #sending a get request and recording the response payload to the variable response
    response = requests.get(url, headers=headers)

    #if the status code is good print the payload to console and record the ship log, otherwise, print the error and record the error log
    if response.status_code > 199 and response.status_code < 300:
        print(response.json())
        log_response(response, 'Ship_Log.txt')
    else:
        print('Error:', response.status_code, response.reason)
        log_response(response, 'error_log.txt')





