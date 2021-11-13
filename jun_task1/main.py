import requests
from config import API_URL

url = API_URL + '10'
response = requests.get(url)

print(response.json()["data"]["last_name"], response.json()["data"]["first_name"])