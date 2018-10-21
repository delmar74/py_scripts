import requests

for i in range(100):
    r = requests.get('http://ya.ru')
    print(r.elapsed)
