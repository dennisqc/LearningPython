lista_reproduccion =[]

numero_canciones = int(input('Cuantas canciones deseas agregar?'))

# iterar
for indice in range(numero_canciones):
    cancion = input(f'Proporciones la camcion {indice +1}: ')
    lista_reproduccion.append(cancion)

lista_reproduccion.append('Hotel California - Eagles')
lista_reproduccion.append('Staying Alive Bee Gees')
lista_reproduccion.append('Dream on - Aerosmith')

#ordernar sort

#lista_reproduccion.sort(reverse=True)
lista_reproduccion.sort()

#mostrar

print(f'\n Lista de Reproducción ')

print(lista_reproduccion)


for musica in lista_reproduccion:
    print(musica)