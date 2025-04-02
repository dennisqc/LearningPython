import requests
from deep_translator import GoogleTranslator

# Inicializar el traductor
translator = GoogleTranslator(source="en", target="es")

city = input("Introduce la ciudad: ")

# URL de OpenWeatherMap con clave de API
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=470451f17c12ace160914acfa089376b&units=metric"

# Obtener los datos del clima
res = requests.get(url)
data = res.json()

if res.status_code == 200:
    temp = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    latitude = data["coord"]["lat"]
    longitude = data["coord"]["lon"]
    description = data["weather"][0]["description"]
    translated_description = translator.translate(description)  # Traducir la descripción
    country = data["sys"]["country"]

    # Mostrar resultados
    print("Temperatura:", temp, "°C")
    print("Descripción:", description)
    print("Descripción traducida al español:", translated_description)
    print("País:", country)
else:
    print("Error: No se encontró la ciudad o hubo un problema con la API.")
