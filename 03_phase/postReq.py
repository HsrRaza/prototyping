import requests

headers = {
    "Authorization":"Bearer my_token",
    "Accept":"application/json"
}

data = {
    "title":"Learning Python",
    "body":"Today I learned  POST request",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data,
    headers=headers
)

print(response.status_code)
print(response.json())