#reduce(function, iterasyon yapılabilcek veritipi(liste vb))
 # reduce fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular ve daha sonra çıkan sonucu
 #listenin 3.elemanına uygular, bu şekilde devam ederek liste bitince bir tane değer döner

from functools import reduce

def topla(x,y):
    return x+y

#print(reduce(topla, [12,18]))
#print(reduce(lambda x,y: x+y, [12,18,10]))

def maksimum(x,y):
    if x>y:
        return x
    else:
        return y

print(reduce(maksimum, [-2,1,5,4,3]))
