import requests

url = 'https://petstore.swagger.io/v2/user/Ivan'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "code": 200,
  "type": "unknown",
  "message": "Ivan"
}

response = requests.delete(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
print(response.json())
print(type(response.json()))