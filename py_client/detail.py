import requests

endpoint = "http://localhost:8000/"

response = requests.get(endpoint + "api/products/3")

print(response.text)
