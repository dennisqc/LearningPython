import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Mi título",
    "body": "Contenido del post",
    "userId": 1
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())
