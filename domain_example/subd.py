import requests

url = "https://spyse.com/api/data/domain/search"
data = { "domain_name" :
        { "operator": "ends",
         "value": ".makyajtrendi.com"}
        }
resp = requests.post(url, json=data)
print(resp.status_code)
#api key , token gibi bir sey lazim 403 donmemesi icin.