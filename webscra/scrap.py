import requests
from bs4 import BeautifulSoup

url = 'https://dockerlabs.es/' 
respuesta = requests.get(url)


if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    maquinas = soup.find_all('div', onclick = True)
    conteo_maquinas=1

    for maquina in maquinas:
        onclick_text = maquina['onclick']
        nombre_maquina = onclick_text.split("'")[1]
        conteo_maquinas+=1

    print(conteo_maquinas)

else:
    print(f'Hubo un error {respuesta.status_code}')