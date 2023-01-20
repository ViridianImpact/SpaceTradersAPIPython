#B0undle55
#Ships_Type_Check.py
#Sends a GET request to the URL https://api.spacetraders.io/systems/OE/ship-listings to view the ship available for purchase in the OE system
#
#
#

import requests
from Logging_Script import log_response

def ships_type_check(token, choice):

    #the URL for viewing ship listings in the OE system
    url = 'https://api.spacetraders.io/systems/OE/ship-listings'

    #header contents
    headers = {
        'Authorization': 'Bearer ' + token
        }

    #data contents
    data = {
        'class': choice
        }

    #sending a get request and recording the response payload to the variable response
    response = requests.get(url, headers=headers, params=data)

    #if the status code is good print the payload to console and record the system log, otherwise, print the error and record the error log
    if response.status_code > 199 and response.status_code < 300:
        print(response.json())
        log_response(response, 'System_Log.txt')
    else:
        print('Error:', response.status_code, response.reason)
        log_response(response, 'error_log.txt')


