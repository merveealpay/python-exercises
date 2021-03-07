import requests

def validate(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.ok:
            #logger.info("Response: OK", data)
            data = response.json()
        else:
            data = {}
        return data
    return wrapper

def new_request(func):
    def wrapper(url):
        result = requests.get(url)
        return result
    return wrapper

@validate
@new_request
def generate_user(url):
    pass



print(generate_user("https://randomuser.me/api/"))