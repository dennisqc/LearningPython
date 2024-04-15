import requests
from googletrans import Translator

translator = Translator()

city = input("introduce la ciudad: ")

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=470451f17c12ace160914acfa089376b&units=metric".format(city)

res = requests.get(url)

data = res.json()

temp = data["main"]["temp"]

wind_speed = data["wind"]["speed"]

latitude = data["coord"]["lat"]
longitude = data["coord"]["lon"]

description = data["weather"][0]["description"]
translated_description = translator.translate(description, src='en', dest='es')
country = data["sys"]["country"]

print("temperatura : ", temp)
print("Descripcion: ", description)
print(f"Descripción traducida al español: {translated_description.text}")
print("Pais:",country)