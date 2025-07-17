import requests

API_KEY = '470451f17c12ace160914acfa089376b'
ciudad = 'Puno'
url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es'

response = requests.get(url)

# Mostrar el contenido completo como diccionario
datos = response.json()

# Imprimirlo de forma legible
import json
print(json.dumps(datos, indent=4, ensure_ascii=False))
