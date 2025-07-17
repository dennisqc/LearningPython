import requests
import json
import os
import datetime

API_KEY = "981aeb5"
HISTORIAL_FILE = "historial.json"

def buscar_pelicula(titulo):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={titulo}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["Response"] == "True":
            mostrar_detalles(data)
            guardar_en_historial(data)
        else:
            print("❌ Película no encontrada")
    else:
        print("⚠️ Error al conectar con la API")

def mostrar_detalles(peli):
    print("\n🎬 Resultados:")
    print(f"🎞️  Título: {peli['Title']}")
    print(f"📅 Año: {peli['Year']}")
    print(f"🎬 Director: {peli['Director']}")
    print(f"⭐ IMDB: {peli['imdbRating']}")

def guardar_en_historial(peli):
    historial = []
    if os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, "r") as f:
            historial = json.load(f)

    entrada = {
        "titulo": peli["Title"],
        "anio": peli["Year"],
        "director": peli["Director"],
        "hora": datetime.datetime.now().isoformat()

    }
    historial.append(entrada)

    with open(HISTORIAL_FILE, "w") as f:
        json.dump(historial, f, indent=4)
    print("📝 Agregado al historial")

def ver_historial():
    if not os.path.exists(HISTORIAL_FILE):
        print("📭 Aún no tienes historial de búsquedas")
        return

    with open(HISTORIAL_FILE, "r") as f:
        historial = json.load(f)

    print("\n📜 Historial de búsquedas:")
    for idx, peli in enumerate(historial, start=1):
        print(f"{idx}. {peli['titulo']} ({peli['anio']}) - Dir: {peli['director']}")

def menu():
    while True:
        print("\n📽️ Menú:")
        print("1. Buscar película")
        print("2. Ver historial")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("🔍 Ingresa el título de la película: ")
            buscar_pelicula(titulo)
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("👋 Hasta luego!")
            break
        else:
            print("❗ Opción no válida")

if __name__ == "__main__":
    menu()
