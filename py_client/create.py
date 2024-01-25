import requests

endpoint = "http://localhost:8000/"

response = requests.post(
    endpoint + "api/products",
    json={"title": "iQOO Neo 7", "description": "A good smart phone", "price": 26000},
)

print(response.text)
