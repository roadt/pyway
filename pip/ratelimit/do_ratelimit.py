from datetime import datetime, timedelta
from ratelimit import limits


FIFTEEN_MINUTES = 900
ONE_DAY=60*60*24

# Define the rate-limited function
@limits(calls=1, period=FIFTEEN_MINUTES)
def my_function():
    # Your function code here
    pass


my_function()
my_function()
my_function()


# call
import requests
FIFTEEN_MINUTES = 900
@limits(calls=1, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response


call_api('https://httpbin.org')
call_api('https://httpbin.org')
