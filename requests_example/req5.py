import requests

#querystring : a way to pass data to the server as part of a get request
#http://www.example.com/?key1=value1&key2=value2
#https://icanhazdadjoke.com/search?term=cat

URL = "https://icanhazdadjoke.com/search"

response = requests.get(url=URL,
                        headers={"Accept": "application/json"},
                        params={"term": "cat", "limit": 1})
data = response.json()
print(data["results"])