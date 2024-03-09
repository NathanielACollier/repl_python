import requests
import curlify
import logging

"""
There is alot of information out there on requests.Session
 + I first found this: https://www.pythonrequests.com/python-requests-interceptor/
 + Then this one used the hooks[] dictionary to set functions that would be called
    + https://alexwlchan.net/2017/requests-hooks/

# curlify docs
+ https://github.com/ofw/curlify

# python logging info
+ https://realpython.com/python-logging/

"""

class nac_http_RequestSession(requests.Session):
    def __init__(self) -> None:
        super().__init__()
        self.hooks['response'] = [self.log_response]

    def log_response(self, *args, **kwargs):
        response = args[0]
        curlCommandText = curlify.to_curl(response.request)
        logging.info(f"""-----------
curl command
------------
{curlCommandText}
------------
""")
        
    