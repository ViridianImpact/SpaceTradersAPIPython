#B0undle55
#Marketplace_Check.py
#makes a get request sent to a specific location marketplace
#
#
#

import requests
from Logging_Script import log_response

#my unique token
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'

#specific url for the marketplace requested 'https://api.spacetraders.io/locations/XX-XX-XX/marketplace'
url = 'https://api.spacetraders.io/locations/OE-PM-TR/marketplace'

#header contents
headers = {
    #token labeled as an authenticaction for the API
    'Authorization': 'Bearer ' + token
    }

#sending a get request and recording the response payload to the variable response
response = requests.get(url, headers=headers)

#if the status code is good print the payload to console and record the marketplace log, otherwise, print the error and record the error log
if response.status_code == 200:
    print(response.json())
    log_response(response, 'Marketplace_Log.txt')    
else:
    print('Error:', response.status_code, response.reason)
    log_response(response, 'error_log.txt')



