import requests

response = requests.get("https://api.agify.io?name=dennis")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
