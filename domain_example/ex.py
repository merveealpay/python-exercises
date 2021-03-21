from requests import request
from bs4 import BeautifulSoup

x = []

def deneme():
    r = request("POST",url="https://domainbigdata.com/", data={"__EVENTTARGET": "search","__EVENTARGUMENT": "merve"
})
    y = BeautifulSoup(r.content, "lxml")
    #find bir tane item, findall birden cok
    t = y.find("table", attrs={"class": "t1"})
    z = t.find("tbody")
    for k in z.findAll("tr"):
        for p in k.findAll("td")[0]:
            #print(p.text)
            x.append(p.text)
deneme()
print(x[1])


