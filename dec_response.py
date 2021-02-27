import time
from functools import wraps

def timer(delay=1):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # fonksiyon calismadan once etkileyebileceğimiz alan

            start = time.time()
            time.sleep(delay)
            response = func(*args, **kwargs)
            # fonksiyon calistiktan sonra etkileyebileceğimiz alan
            end = time.time()
            print(end - start)
            print("OK")

            return response
        return wrapper
    return dec


@timer(delay=10)
def test(name):
    time.sleep(4)
    print("Katlamalı Bal yiyen Merve")

test("ok")