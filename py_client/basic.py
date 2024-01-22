import requests

endpoint = "http://localhost:8000/"

response = requests.post(
    endpoint + "api/products/create",
    json={
        "title": "Samsung S24 Ultra",
        "description": "Pretty good phone but s23 ultra is better",
        "price": "124000",
    },
)

print(response.text)
