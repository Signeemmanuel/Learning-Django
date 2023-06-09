import requests

endpoint = "http://localhost:8000/api/products/7/update/"
data = {
    "title": "Security Management",
    "content": "This is an introductory Course to Security Management"
}
get_response =  requests.put(endpoint, json=data)

print(get_response.json())