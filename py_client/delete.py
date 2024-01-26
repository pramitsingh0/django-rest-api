import requests

endpoint = "http://localhost:8000/"

response = requests.delete(
    endpoint + "api/products/1/delete"
)

print(response.text)
