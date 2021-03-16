import json
import requests

# istek atarken ozel headers gonderebiliriz, dict format
r = requests.post("http://httpbin.org/post", headers={"User-Agent": "Merve-Chrome"})
# print(r.status_code)


# istek atilan sitenin html icerigini dondurur
r_v2 = requests.get("http://httpbin.org/")
#print(r_v2.text)
# status kod historysi
#print(r_v2.history)
#sayfanin encode degeri
reqEncode = r_v2.encoding
print(reqEncode)
#yapilan istegin cesidi
reqWhat = r_v2.request
print(reqWhat)
#gecen zaman
print(r_v2.elapsed.total_seconds())
