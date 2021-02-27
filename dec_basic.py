import requests

def decorator(func):
    def wrapper(*args, **kwargs):
        response = func()
        return response
    return wrapper

@decorator
def test(name):
    print(name)

@decorator
def test2(lastname):
    print(lastname)

test(name="mERVE")
test2(lastname="alpay")

