import requests

endpoint = "http://localhost:8000/"

response = requests.put(
    endpoint + "api/products/1/update",
    json={"title": "hello", "description": "world", "price": 43},
)

print(response.text)
