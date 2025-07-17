import requests

pais = "Peru"
url = f"https://restcountries.com/v3.1/name/{pais}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()[0]
    print(f"🌍 {data['name']['common']}")
    print(f"Capital: {data['capital'][0]}")
    print(f"Población: {data['population']}")
    print(f"Moneda: {list(data['currencies'].keys())[0]}")
else:
    print("País no encontrado")
