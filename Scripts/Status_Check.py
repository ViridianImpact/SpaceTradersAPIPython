#B0undle55
#Status_Check.py
#Sends a GET request to the URL https://api.spacetraders.io/game/status to view the status of the API spacetraders
#
#
#

import requests
from Logging_Script import log_response

def status_check():
    
    #the URL for requesting the game status
    url = 'https://api.spacetraders.io/game/status'

    #sending a get request and recording the response payload to the variable response
    response = requests.get(url)

    #if the status code is good print the payload to console and record the game log, otherwise, print the error and record the error log
    if response.status_code == 200:
        print(response.json())
        log_response(response, 'Game_Log.txt')
    else:
        print('Error:', response.status_code, response.reason)
        log_response(response, 'error_log.txt')
