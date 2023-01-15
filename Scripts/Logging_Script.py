#B0undle55
#Logging_Script.py
#Creates an append to the end of the persistent log provided by the arguments
#
#
#

import json

def log_response(response, filename):
    """
    Logs the Payload response of a request to a file.
    :param response: The response of the request.
    :param filename: The name of the file for the log.
    """
    with open(filename, 'a') as outfile:
        json.dump(response.json(), outfile)
        outfile.write("\n")
