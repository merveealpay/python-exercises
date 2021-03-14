import requests

# GET

r = requests.get("http://httpbin.org/get", params={"kategori": "elektronik", "marka": "apple"})
# print(r.url)
# output : http://httpbin.org/get?kategori=elektronik&marka=apple

# bazen istek attigimiz sayfa baska bir sayfaya yonleniyor olabilir
# allow_redirects=False -> yonlendirmeyi kapatir.

r_v2 = requests.get("http://httpbin.org/redirect/1", allow_redirects=True)
# print(r_v2.status_code)

# POST

r_v3 = requests.post("http://httpbin.org/post", data={"username": "merve", "pass": "123asd"})
# print(r_v3.status_code)
response = r_v3.json()
form = response["form"]
# print(form)

# timeout suresince cevap donmezse hata vercektir.
r_v4 = requests.get("http://httpbin.org/get", timeout=1)
