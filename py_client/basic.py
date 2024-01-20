import requests

endpoint = "http://localhost:8000/"

response = requests.get(endpoint + "api/", json={"product_id": 1})

print(response.json())
