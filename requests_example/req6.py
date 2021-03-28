import requests
from random import choice

user_inp = input("search for : ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(url=url,
                        headers={"Accept": "application/json"},
                        params={"term": user_inp}).json()

results = response["results"]
num_jokes = response["total_jokes"]
if num_jokes > 1:
    print("there are many jokes")
    print(choice(results)['joke'])
elif num_jokes == 1:
    #print(response["results"][0]['joke'])
    print("there is one joke")
    print(results[0]['joke'])
else:
    print("there are no jokes")