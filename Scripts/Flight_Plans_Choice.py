#B0undle55
#Flight_Plan_Check.py
#Sends a POST request to the URL https://api.spacetraders.io/my/flight-plans to assign a flight plan
#
#
#

import requests
from Logging_Script import log_response

"""
token; my personal token for authentication
shipID; the Ship ID for the ship that will be assigned to the flight plan
destination; the destination selected for the flight plan
"""
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
shipID = 'clcwsbzgc107055215s63c83vr0d'
destination = 'OE-PM'

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



