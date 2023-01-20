#B0undle55
#Ship_Choice.py
#Sends a POST request to the URL https://api.spacetraders.io/my/ships to request a purchase of the specified ship
#
#
#

import requests
from Logging_Script import log_response

def ship_choice(token, choice, location):

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
    if response.status_code > 199 and response.status_code < 300:
        print(response.json())
        log_response(response, 'Vehicle_Log.txt')
    else:
        print('Error:', response.status_code, response.reason)
        log_response(response, 'error_log.txt')

