import requests
from typing import Optional, Union

BASE_URL = "https://randomuser.me/api"


def test(size: Optional[int] = 1):
    params = {"results": size}
    response = requests.get(url=BASE_URL, params=params)
    return response
    if not response.ok:
        return []
    
    data = response.json()

    results = data['results']


    for item in results:
        new_data = {}
        new_data['gender'] = item['gender']
        new_data['title'] = item['name']['title']
        new_data['firstname'] = item['name']['first']
        new_data['lastname'] = item['name']['last']
        new_data['date'] = item['dob']['date']
        new_data['age'] = item['dob']['age']
        yield new_data


# data_list = list(test(size=10))


data = [
    {
        "names" : [{"name":"merve"},{"name": "merve su"}],
        "lastname": "Alpay"
    },
    {
        "names" : [{"name":"merve"},{"name": "merve su"}],
        "lastname": "Alpay"
    }
]

# for item in data:
#    names = [i for i in item["names"]]
#    lastname = item["lastname"]


from typing import List

# Nested function
def first(age: int) -> List[int]:
    def last(new_age: int)->int:
        return new_age * 2
    return [last(age)]

# print(first(2))

def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)


# decorator

def test(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@test
def test_first():
    return 10


