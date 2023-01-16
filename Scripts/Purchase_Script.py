#B0undle55
#Purchase_Script.py
#Sends a POST request to the URL https://api.spacetraders.io/my/purchase-orders to submit a purchase order for 20 Units of FUEL
#
#
#

import requests
from Logging_Script import log_response

def purchase(token, shipID, good, quantity):

    #specific URL for the assignment of purchase orders
    url = 'https://api.spacetraders.io/my/purchase-orders'

    #header contents
    headers = {
        #token labeled as an authenticaction for the API
        'Authorization': 'Bearer ' + token
        }

    #data contents
    data = {
        #shipID, good and quantity for the purchase order
        'shipId': shipID,
        'good': good,
        'quantity': quantity
        }

    #sending a post request and recording the response payload to the variable response
    response = requests.post(url, json=data, headers=headers)

    #if the status code is good print the payload to console and record the purchase log, otherwise, print the error and record the error log
    if response.status_code == 200 or response.status_code == 201:
        print(response.json())
        log_response(response, 'Purchase_Log.txt')
    else:
        print('Error:', response.status_code, response.reason)
        log_response(response, 'error_log.txt')


