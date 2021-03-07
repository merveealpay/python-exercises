# - *- coding: utf- 8 - *-

# map(fonksiyon, iterasyon yapılabilecek veritipi(liste,demet vs...))
# map fonksiyonun ilk parametresi fonksiyon objesidir.
# gönderilen fonksiyonu her bir eleman üzerinde uygulayarak sonuçları map objesi olarak dönüyor

#map example:

def double(x):
    return x*2

map(double, [1,2,3,4])
test = list(map(double, [1,2,3,4]))
#print(test)

#lambda-map example:

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]

test2 = list(map(lambda x,y : x*y, liste1, liste2))

print(test2)