import requests

url = 'https://petstore.swagger.io/v2/user/Ivan'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "code": 200,
  "type": "unknown",
  "message": "9223372036854746000"
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
print(response.json())
print(type(response.json()))