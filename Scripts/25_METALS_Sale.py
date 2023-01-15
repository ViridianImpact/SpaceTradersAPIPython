#B0undle55
#25_METALS_Purchase.py
#Sends a POST request to the URL https://api.spacetraders.io/my/purchase-orders to submit a purchase order for 25 Units of METAL
#
#
#

import requests

"""
token; my personal token for authentication
shipID; the Ship ID of the ship that is to be unloaded
good; the item name to be sold
quantity; the quantity of the item to be sold
"""
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
shipID = 'clcwsbzgc107055215s63c83vr0d'
good = 'METALS'
quantity = 25

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
if response.status_code == 200:
    print(response.json())
    log_response(response, 'Sale_Log.txt')
else:
    print('Error:', response.status_code, response.reason)
    log_response(response, 'error_log.txt')

# token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
# user = 'ViridianImpact'
# shipID = 'clcwsbzgc107055215s63c83vr0d'




