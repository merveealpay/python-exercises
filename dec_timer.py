# - *- coding: utf- 8 - *-

#decorator fonksiyonlar, pythonda fonksiyonlarımızın dinamik olarak ekstra özellik ekledigimiz fonksiyonlarıdr
#kod tekrarını engeller
#flask django gibi frameworklerde cok kullanılır

import time

def calculate_time(func):
    def wrapper(numbers):
        start = time.time()

        result = func(numbers)

        end = time.time()

        print(func.__name__ + " " + str(end-start) +  " saniye surdu.")
        return result
    return wrapper

@calculate_time
def square(numbers):
    result = list()

    for i in numbers:
        result.append(i**2)
    
    return result

@calculate_time
def cube(numbers):
    result = list()

    for i in numbers:
        result.append(i**3)

    return result

square(range(500))
cube(range(500))

