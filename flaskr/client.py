import requests

response = requests.get('http://127.0.0.1:6379/current')

data = response.text

print('The current game is: ', data)