#B0undle55
#Flight_Plan_Check.py
#Sends a GET request to the URL https://api.spacetraders.io/my/flight-plans to view the fight plan
#
#
#

import requests
from Logging_Script import log_response

"""
token; my personal token for authentication
flightID; the Flight ID for the flight plan that is to be viewed
"""
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
flightID = 'clcwsxa6y108894215s6lnj3ggao'

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
if response.status_code == 200:
    print(response.json())
    log_response(response, 'Flight_Log.txt')
else:
    print('Error:', response.status_code, response.reason)
    log_response(response, 'error_log.txt')

# token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
# user = 'ViridianImpact'
# shipID = 'clcwsbzgc107055215s63c83vr0d'
# flightID = 'clcwsxa6y108894215s6lnj3ggao'




