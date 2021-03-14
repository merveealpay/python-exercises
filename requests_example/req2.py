import json
import requests

endpoint = "http://httpbin.org/post"
myData = {
    "id": 1,
    "name": "merve",
    "email": "merveealpay@gmail.com",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
             "lng": "81.1496"
       }
    }
}

r = requests.post(endpoint, data=json.dumps(myData))
# print(r.status_code)
# print(r.content)
#print(r.cookies)
print(r.headers)