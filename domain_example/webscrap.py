import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.producthunt.com")
#source=html
#lxml,html.parser,lxml-xml,html5lib
source = BeautifulSoup(r.content, "lxml")

#title tag
#print(source.title)

#find(value)-> sayfadaki ozel degeri cektirir
#print(source.find("p"))

#html etiketlerini kaldir sadece yaziya ulas ->> text
#print(source.find("p").text)

#producthunt sitesindeki API Conn baglanti adresi
print(source.find("h3", attrs={"class": "styles_font__2Nqit styles_medium__3fSwd styles_semiBold__2IC3i styles_title__1pqJi styles_lineHeight__2RYYy styles_underline__20yPd"}).text)
