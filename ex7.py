import requests

def validate(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.ok:
            data = response.json()
            #logger.info("Response: OK", data)
            f = open("success.txt", "a")
            f.write("Response: OK ---- \n")
            f.write(str(data))
            f.write("\n")
            f.close()
        else:
            #data = {}
            f = open("error.txt", "a")
            f.write("Response: ERROR ---- \n")
            data = str(response.status_code) + " " + response.text 
            f.write(data)
            f.write("\n")
            f.close()
        return data
    return wrapper

def new_request(func):
    def wrapper(url):
        result = requests.get(url)
        return result
    return wrapper


@validate
@new_request
def generate_user(url):
    pass


print(generate_user("https://randomuser.me/api/"))
#print(generate_user("https://randomuser.me/merve"))