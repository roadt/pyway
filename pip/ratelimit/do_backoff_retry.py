
from ratelimit import limits, RateLimitException
from backoff import on_exception, expo

import requests

ONE_MINUTE = 60
FIFTEEN_MINUTES = 900

@on_exception(expo, RateLimitException, max_tries=8)
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
