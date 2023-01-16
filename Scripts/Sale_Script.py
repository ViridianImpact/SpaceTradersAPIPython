#B0undle55
#25_METALS_Purchase.py
#Sends a POST request to the URL https://api.spacetraders.io/my/purchase-orders to submit a purchase order for 25 Units of METAL
#
#
#

import requests
from Logging_Script import log_response

def sale(token, shipID, good, quantity):

    #specific URL for the assignment of sell orders
    url = 'https://api.spacetraders.io/my/sell-orders'

    #header contents
    headers = {
        #token labeled as an authenticaction for the API
        'Authorization': 'Bearer ' + token
        }

    #data contents
    data = {
        #shipID, good and quantity for the sell order
        'shipId': shipID,
        'good': good,
        'quantity': quantity
        }

    #sending a post request and recording the response payload to the variable response
    response = requests.post(url, json=data, headers=headers)

    #if the status code is good print the payload to console and record the sale log, otherwise, print the error and record the error log
    if response.status_code > 199 and response.status_code < 300:
        print(response.json())
        log_response(response, 'Sale_Log.txt')
    else:
        print('Error:', response.status_code, response.reason)
        log_response(response, 'error_log.txt')
        
        