# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json
from pprint import pprint

username = 'aeroswitch'
main_link = f'https://api.github.com/users/{username}/repos'

params = {
    'accept': 'application/vnd.github.v3+json',
    'username': username
}

response = requests.get(main_link, params=params)
json_data = response.json()

pprint(json_data)

with open('API_response.json', 'w') as f:
    json.dump(json_data, f)
