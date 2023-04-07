
from ratelimit import limits, sleep_and_retry

import requests

ONE_MINUTES=60
FIFTEEN_MINUTES = 900

@sleep_and_retry
@limits(calls=2, period=10)
def call_api(url):
    response = requests.get(url)
    print(url)
    
    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response

  
call_api("https://httpbin.org/get")
call_api("https://httpbin.org/get")
call_api("https://httpbin.org/get")
