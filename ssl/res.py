import requests

url = "www.example.com"

if not url.strip().startswith("http"):
    x = "http://" + url
    print(x)
    res = requests.get(x)
    status = res.status_code
    print(status)
else:
    print(url[7:])

if status == 200:
    # ssl check et.
    print("ssl check ediliyor")
