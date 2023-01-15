#B0undle55
#Status_Check.py
#Sends a GET request to the URL https://api.spacetraders.io/users/XXXXXXXXXX/claim to request a username
#
#
#

import requests
from Logging_Script import log_response

#username; the username being requested
username = 'ViridianImpact'

#the URL to request a username with the specified username loaded
url = 'https://api.spacetraders.io/users/' + username + '/claim'

#sending a post request and recording the response payload to the variable response
response = requests.post(url)

#if the status code is good print the payload to console and record the game log, otherwise, print the error and record the error log
if response.status_code == 200:
    print(response.json())
    log_response(response, 'Game_Log.txt')
else:
    print('Error:', response.status_code, response.reason)
    log_response(response, 'error_log.txt')

# token = 4b0325e4-e972-4a4d-b67f-5cdd87d62f67
# user = ViridianImpact