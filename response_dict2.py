import requests

URL = "https://randomuser.me/api/"

def test():
    params = {'results': 5}
    for i in range(5):
        response = requests.get(url=URL, params=params)
        data = response.json()
        newData = {}
        newData['gender'] = data['results'][i]['gender']
        newData['title'] = data['results'][i]['name']['title']
        newData['firstname'] = data['results'][i]['name']['first']
        newData['lastname'] = data['results'][i]['name']['last']
        newData['date'] = data['results'][i]['dob']['date']
        newData['age'] = data['results'][i]['dob']['age']
        yield newData

dataList = list(test())

print(dataList)