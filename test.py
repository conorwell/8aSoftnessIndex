import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "getIndex/ben-blackmore")
print(response.json())
response = requests.get(BASE + "getIndex/ben-blackmore")
print(response.json())
response = requests.get(BASE + "getIndex/manny-kahne")
print(response.json())
response = requests.patch(BASE+"getIndex/conor-wellman")
print(response.json())
