import requests
import backoff
from requests.exceptions import ConnectionError, HTTPError

@backoff.on_exception(
        backoff.expo, requests.exceptions.RequestException,
                    max_tries=3)
def get_response(url):
    response = requests.get(url)
    return response

print(get_response("https://randomuser.me/merve/"))

#backoff modul, bir fonksiyon belli kosullar karsilanana kadar yeniden denenecek
#sekilde sarmak icin kullanilabilen dekoratorleri saglar.

#@backoff.on_exception decoratoru, belli bir hata ciktiginda yeniden denemek icin
