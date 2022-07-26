import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + 'Video/1', {'likes': 10, 'name': 'hi', 'view': 1000})
print(response.json())

input()

response = requests.get(BASE + 'Video/1')
print(response.json())