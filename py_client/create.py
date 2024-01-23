import requests

endpoint = "http://localhost:8000/"

response = requests.post(
    endpoint + "api/products",
    json={"title": "Logitech G102", "description": "A good mouse", "price": 1600},
)

print(response.text)
