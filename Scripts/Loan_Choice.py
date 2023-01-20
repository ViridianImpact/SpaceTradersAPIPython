#B0undle55
#Loan_Check.py
#Sends a POST request to the URL https://api.spacetraders.io/my/loans to obtain the selected loan type
#
#
#

import requests
from Logging_Script import log_response

def loan_choice(token, choice):

    #the URL to be queried for loans requests
    url = 'https://api.spacetraders.io/my/loans'

    #headers contents
    headers = {
        'Authorization': 'Bearer ' + token
        }

    #data contents
    data = {
        'type': choice
        }

    #sending a post request and recording the response payload to the variable response
    response = requests.post(url, json=data, headers=headers)

    #if the status code is good print the payload to console and record the loan log, otherwise, print the error and record the error log
    if response.status_code > 199 and response.status_code < 300:
        print(response.json())
        log_response(response, 'Loan_Log.txt')
    else:
        print('Error:', response.status_code, response.reason)
        log_response(response, 'error_log.txt')

