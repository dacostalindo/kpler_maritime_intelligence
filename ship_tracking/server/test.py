import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "ship/5091")
print(response.json())