import requests

endpoint = "http://localhost:8000/"

response = requests.get(endpoint + "api/products")

print(response.text)
