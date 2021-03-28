import requests

URL = "https://icanhazdadjoke.com/"

# response = requests.get(url=URL, headers={"Accept": "text/plain"})
response = requests.get(url=URL, headers={"Accept": "application/json"})
# print(type(response.text))
data = response.json()
print(data["joke"])
print("status : {}".format(data["status"]))
