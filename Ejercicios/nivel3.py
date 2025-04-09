#🟠 Nivel 3: Funciones y diccionarios
#Función para verificar palíndromos
#
#Crea una función que reciba una palabra y devuelva si es palíndromo o no.
#

def palindromo(palabra):
    palabra = palabra.lower()
    
    if palabra == palabra[::-1]:
        return True
    else:
        return False

palabra = input("Introduce una palabra para verificar si es palíndromo: ")

if palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

#Conversión de minutos a horas y minutos
#
#Por ejemplo, 130 minutos = 2 horas y 10 minutos.
#

def tiempo(minutos):
    horas = minutos//60
    minutos_restantes = minutos%60 
    return horas , minutos_restantes

minutos = int(input("Introduce los minutos: "))

horas, minutos_restantes = tiempo(minutos)

print("son :", horas, " hora con :" ,minutos_restantes," minutos")


#Contador de palabras
#
#Pide al usuario una frase y cuenta cuántas palabras tiene.
#


frase = (input("introduce una frase: "))

palabras = len((frase.split()))

print("tiene ",palabras, " palabras que conforman")


#Diccionario de contactos
#
#Guarda nombres y teléfonos en un diccionario. Permite buscar por nombre.
#

# Diccionario de contactos
contactos = {
    "Juan": "123-456-789",
    "Ana": "987-654-321",
    "Pedro": "555-666-777",
    "Maria": "444-555-666"
}

# Solicitar al usuario el nombre del contacto que desea buscar
nombre = input("Introduce el nombre del contacto que buscas: ")

# Buscar el contacto en el diccionario
if nombre in contactos:
    print(f"El teléfono de {nombre} es: {contactos[nombre]}")
else:
    print("El contacto no existe en el diccionario.")




#Calculadora con funciones
#
#Implementa una calculadora usando funciones: suma, resta, multiplicación y división.

# Funciones para las operaciones
