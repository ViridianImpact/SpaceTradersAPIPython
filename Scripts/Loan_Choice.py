#B0undle55
#Loan_Check.py
#Sends a POST request to the URL https://api.spacetraders.io/my/loans to obtain the selected loan type
#
#
#

import requests
from Logging_Script import log_response

"""
token; my personal token for authentication
choice; the loan type of the loan requested
"""
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
choice = 'STARTUP'

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
if response.status_code == 200:
    print(response.json())
    log_response(response, 'Loan_Log.txt')
else:
    print('Error:', response.status_code, response.reason)
    log_response(response, 'error_log.txt')

# token = 4b0325e4-e972-4a4d-b67f-5cdd87d62f67
# user = ViridianImpact

