import requests

endpoint = "http://localhost:8000/"

response = requests.post(
    endpoint + "api/products",
    json={"title": "Milton 1ltr Water Bottle", "description": "Blue Color", "price": 35},
)

print(response.text)
