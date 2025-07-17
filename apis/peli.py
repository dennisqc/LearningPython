

import requests

API_KEY = "981aeb5"
pelicula = "Interstellar"
url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={pelicula}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"🎥 Título: {data['Title']}")
    print(f"Año: {data['Year']}")
    print(f"Director: {data['Director']}")
    print(f"IMDB Rating: {data['imdbRating']}")
else:
    print("Error al consultar película")
