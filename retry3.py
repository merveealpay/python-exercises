import requests 
from retry import retry
from requests.exceptions import ConnectionError, HTTPError


@retry(exceptions=ConnectionError, tries=3, delay=1, backoff=2, logger=None)
def get_page(): 
    #response = requests.get('https://randomuser.me/')
    response = requests.get('https://randomuser.me/api/')
    return response.json() 