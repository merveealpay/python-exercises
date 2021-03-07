import requests
import backoff

def new_request(func):
    def wrapper(url):
        result = requests.get(url)
        return result
    return wrapper

def validate(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.ok:
            data = response.json()
        else:
            data = {}
        return data
    return wrapper                        

@validate
#@backoff.on_exception(backoff.expo, requests.exceptions.RequestException,max_tries=3)
@new_request
def generate_user(url):
    pass


#print(generate_user("https://randomuser.me/api/"))
print(generate_user("https://randomuser.me/merve/"))

#backoff modul, bir fonksiyon belli kosullar karsilanana kadar yeniden denenecek
#sekilde sarmak icin kullanilabilen dekoratorleri saglar.

#@backoff.on_exception decoratoru, belli bir hata ciktiginda yeniden denemek icin
