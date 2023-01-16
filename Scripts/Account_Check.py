#B0undle55
#Account_Check.py
#Sends a get request to https://api.spacetraders.io/my/account with my key in the header for an overview of my account
#
#
#

import requests
from Logging_Script import log_response

def account_check(token):
    
    #the URL for checking accounts
    url = 'https://api.spacetraders.io/my/account'

    #the header contents
    headers = {
        #token labeled as an authenticaction for the API
        'Authorization': 'Bearer ' + token
        }

    #sending a get request and recording the response payload to the variable response
    response = requests.get(url, headers=headers)

    #if the status code is good print the payload to console and record the account log, otherwise, print the error and record the error log
    if response.status_code == 200:
        print(response.json())
        print('\n')
        log_response(response, 'Account_Log.txt')
        #return None
    else:
        print('Error:', response.status_code, response.reason)
        print('\n')
        log_response(response, 'error_log.txt')
        #return None
