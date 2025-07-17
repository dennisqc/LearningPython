import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    tasa_pen = data["rates"]["PEN"]
    print(f"💱 1 USD = {tasa_pen} PEN")
else:
    print("Error al consultar tipo de cambio")
