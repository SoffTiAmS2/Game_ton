import requests

import json


# Ваш токен

token = 'b1bab484-2d75-4f8d-bb4c-bf0e0f468e36'

# URL сервера

server_url = 'https://games-test.datsteam.dev/play/snake3d'


# API-метод

api = '/player/move'

url = f"{server_url}{api}"


# Данные для отправки

data = {

    'snakes': []

}


# Заголовки запроса

headers = {

    'X-Auth-Token': token,

    'Content-Type': 'application/json'

}


# Выполнение POST-запроса

response = requests.post(url, headers=headers, json=data)


# Сохранение ответа в файл

with open('example_response.json', 'w') as file:

    file.write(response.text)

