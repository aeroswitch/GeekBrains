# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json
from pprint import pprint
from base64 import b64encode

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

# 2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое,
# требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

# I'll use the public API for Cloud Data Protection provided by Acronis. It is not listed in the link above,
# but I work in this company and I'd like to learn more about our API


# follow instructions available in the API guide:
# https://developer.acronis.com/doc/account-management/v2/guide/getting-started/authenticating

# After registering an API client in Acronis Cloud platform:
client_id = '73d7a7a8-9e27-4032-9340-a6c9283a8cea'
client_secret = 'f4d7d6a0bd4049708f17ee06d26a3891'
datacenter_url = 'https://eu2-cloud.acronis.com'
base_url = f'{datacenter_url}/api/2'

# Issuing the API client an access token
encoded_client_creds = b64encode(f'{client_id}:{client_secret}'.encode('ascii'))
basic_auth = {
    'Authorization': 'Basic ' + encoded_client_creds.decode('ascii')
}

response_acronis = requests.post(f'{base_url}/idp/token',
                          headers={'Content-Type': 'application/x-www-form-urlencoded',
                                   **basic_auth},data={'grant_type': 'client_credentials'})
print(response_acronis.status_code)

token_info = response_acronis.json()
pprint(token_info)
auth = {'Authorization': 'Bearer ' + token_info['access_token']}
print(auth)

requests.get(f'{base_url}/clients/{client_id}', headers=auth)

# example of API call: Fetching available offering items
# https://developer.acronis.com/doc/account-management/v2/guide/offering-items/fetching-available-ois

tenant_id = '34e55d14-9e04-4199-9e28-203ce0c07d66'

response_offering_items = requests.get(f'{base_url}/tenants/{tenant_id}/offering_items', headers=auth)
print(response_offering_items.status_code)
pprint(response_offering_items.json())

acronis_json_data = response_offering_items.json()

with open('Acronis_API_response.json', 'w') as f:
    json.dump(acronis_json_data, f)





