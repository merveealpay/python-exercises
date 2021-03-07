class Car():
    model = "BMW"
    color = "Red"

car1 = Car()
#print(car1)
#print(car1.color)

#her bir objeyi baslangicta farkli degerlerle olusturmamiz icin her bir objeyi
#olustururken objelerin degerlerini gondermemiz gerekiyor.
#bunun icin __init__() metodu kullaniriz.

#init metodu constructor fonksiyondur, objelerimiz olusturulurken otomatik olarak
#ilk cagrilan fonksiyondur. Bu metodu ozel olarak tanimlayarak objelerimizi farkli 
#degerlerle olusturabiliriz

#init'i cagirmadik ama kendi kendine cagrildi nesneyi olustururken.
#burdaki self ise, objeyi olusturdugmuz zaman o objeyi gosteren bir referans
#metodlarimizda en basta bulunmasi gereken parametre, yani bir objenin
#butun ozelliklerini ve metodlarini bu referans uzerinden kullanabiliriz.

class NewCar():

    def __init__(self, model, renk):
        print("init fonk cagrildi")
        self.model = model
        self.renk = renk

car2 = NewCar("bmw", "kirmizi")
car3 = NewCar("renault", "mavi")

print(car2.model)
print(car3.model)