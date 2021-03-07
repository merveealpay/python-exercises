# - *- coding: utf- 8 - *-


#filter(fonksiyon,iterasyon yapılabilen veritipi(liste vb))
#filter() fonksiyonu birinci parametre olarak mutlaka boolean deger dönen fonksiyon alır
#liste gibi veri tiplerinin her bir elemanına bu fonksiyonu uygular
#filter sadece True sonuç çıkaran degerleri alarak bir tane filter objesi döner

#cift sayilari getir

filter(lambda x : x % 2 == 0,[1,2,3,4,5,6])
liste = list(filter(lambda x : x % 2 == 0,[1,2,3,4,5,6]))
#print(liste)

#asallık

def asal_mi(x):
    i = 2

    if ( x == 1):
        return False
    elif (x == 2):
        return True
    else:
        while(i < x):
            if( x % i == 0):
                return False
            i += 1
        return True

#print(asal_mi(8))
print(filter(asal_mi, range(1,100)))