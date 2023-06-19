import requests

url = 'https://petstore.swagger.io/v2/user/Ivan'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "id": 9223372036854746000,
  "username": "Ivan",
  "firstName": "Ivan",
  "lastName": "Ivanov",
  "email": "ivan.ivanov@mail.ru",
  "password": "IvAn123",
  "phone": "+79777777777",
  "userStatus": 0
}

response = requests.get(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
print(response.json())
print(type(response.json()))