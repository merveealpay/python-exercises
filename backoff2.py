import requests
import backoff
from requests.exceptions import ConnectionError, HTTPError

@backoff.on_predicate(backoff.constant, max_tries=4, interval=1)
def get_response(url):
    print("ok")
    response = requests.get(url)
    return response

print(get_response("https://randomuser.me/api/"))

#backoff modul, bir fonksiyon belli kosullar karsilanana kadar yeniden denenecek
#sekilde sarmak icin kullanilabilen dekoratorleri saglar.

#@backoff.on_exception decoratoru, belli bir hata ciktiginda yeniden denemek icin
