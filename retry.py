import requests
#import backoff
import time
from functools import wraps
from requests.exceptions import ConnectionError, Timeout



URL = "https://randomuser.me/merve/"

# @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2)
# def get_response(*args):
#     try:
#         res = requests.get(URL)
#         data = res.json()
#     except Exception:
#         data = res.status_code
#     return data

# print(get_response())

def retry(exceptions, tries=4, delay=3, backoff=2, logger=None):
    """
    Retry calling the decorated function using an exponential backoff.

    Args:
        exceptions: The exception to check. may be a tuple of
            exceptions to check.
        tries: Number of times to try (not retry) before giving up.
        delay: Initial delay between retries in seconds.
        backoff: Backoff multiplier (e.g. value of 2 will double the delay
            each retry).
        logger: Logger to use. If None, print.
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions as e:
                    msg = '{}, Retrying in {} seconds...'.format(e, mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry

# @retry(requests.exceptions.Timeout)
# def call_api():
#     return requests.get(URL)

@retry(Exception, tries=6)
def call_api():
    return requests.get(URL)

print(call_api())
#http://httpstat.us/503