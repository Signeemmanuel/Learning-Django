import requests

endpoint = "http://localhost:8000/api/products/7/delete/"

get_response =  requests.delete(endpoint)

print(get_response.status_code)