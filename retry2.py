import requests
from retry import retry


URL = "https://randomuser.me/merve/"

def get_res(*args):
    res = requests.get(URL)
    if res.ok:
        data = res.json()
    else:
        data = res.status_code
    return data

@retry(get_res, tries=3, delay=2)
def handle():
    return "3 kez denedi 2 saniye arayla"

print(handle())