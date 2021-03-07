import requests
import backoff

#The on_exception decorator is used to retry
# when a specified exception is raised.
#specify conditions under which to give up.

def fatal_code(e):
    return 400 <= e.response.status_code < 500

@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_tries=5,
                      giveup=fatal_code)
def get_url(url):
    return requests.get(url)

print(get_url('https://randomuser.me/merve/'))