#B0undle55
#Flight_Plan_Check.py
#Sends a POST request to the URL https://api.spacetraders.io/my/flight-plans to assign a flight plan
#
#
#

import requests
from Logging_Script import log_response

def flight_plans_choice(token, shipID, destination):

    #the URL to be queried with the variable for the specific flight requested appended to the end
    url = 'https://api.spacetraders.io/my/flight-plans'

    #header contents
    headers = {
        #token labeled as an authenticaction for the API
        'Authorization': 'Bearer ' + token
        }

    #data contents
    data = {
        'shipId': shipID,
        'destination': destination
        }

    #sending a post request and recording the response payload to the variable response
    response = requests.post(url, json=data, headers=headers)

    #if the status code is good print the payload to console and record the flight log, otherwise, print the error and record the error log
    if response.status_code > 199 and response.status_code < 300:
        print(response.json())
        log_response(response, 'Flight_Log.txt')
    else:
        print('Error:', response.status_code, response.reason)
        log_response(response, 'error_log.txt')