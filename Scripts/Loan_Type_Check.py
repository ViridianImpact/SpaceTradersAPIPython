#B0undle55
#Loan_Type_Check.py
#Sends a GET request to the URL https://api.spacetraders.io/types/loans to view the loans available to the account specified
#
#
#

import requests
from Logging_Script import log_response

#my personal token
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'

#the URL to be queried for viewing loans
url = 'https://api.spacetraders.io/types/loans'

#headers
headers = {
    'Authorization': 'Bearer ' + token
    }

#sending a get request and recording the response payload to the variable response
response = requests.get(url, headers=headers)

#if the status code is good print the payload to console and record the loan log, otherwise, print the error and record the error log
if response.status_code == 200:
    print(response.json())
    log_response(response, 'Loan_Log.txt')
else:
    print('Error:', response.status_code, response.reason)
    log_response(response, 'error_log.txt')

