import requests

def validate(BASE_URL=""):
    def decorator(func):
        def wrapper():
           params = {"resulsts": 1}
           response = requests.get(url=BASE_URL, params=params)
           if not response.ok:
               return []
           data = response.json()
           print(data)
        return wrapper
    return decorator

@validate(BASE_URL="https://randomuser.me/api")
def test():
    pass

test()

