#B0undle55
#Flight_Plan_Check.py
#Sends a GET request to the URL https://api.spacetraders.io/my/flight-plans to view the fight plan
#
#
#

import requests
from Logging_Script import log_response

def flight_plan_check(token, flightID):

    #the URL to be queried with the variable for the specific flight requested appended to the end
    url = 'https://api.spacetraders.io/my/flight-plans/' + flightID

    #the header contents
    headers = {
        #token labeled as an authenticaction for the API
        'Authorization': 'Bearer ' + token
        }

    #sending a get request and recording the response payload to the variable response
    response = requests.get(url, headers=headers)

    #if the status code is good print the payload to console and record the flights log, otherwise, print the error and record the error log
    if response.status_code > 199 and response.status_code < 300:
        print(response.json())
        log_response(response, 'Flight_Log.txt')
    else:
        print('Error:', response.status_code, response.reason)
        log_response(response, 'error_log.txt')