import requests


# endpoint = "https://www.github.com"
endpoint = "http://localhost:8000/api/products/1"

get_response = requests.get(endpoint)
# get_response = requests.post(endpoint, json={"title": "Learning Django", "content": "Django for Biginners", "price": 250.50})
print(get_response.json())