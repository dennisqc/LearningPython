#🟡 Nivel 2: Control de flujo y listas
#Contador del 1 al 10
#
#Usa un bucle for o while para contar del 1 al 10.

#for i in range(1, 11):
#    print(i)

contador = 1

while contador <= 10:
    print(contador)   
    contador += 1

 
print('Fin del ciclo while')

#
#Suma de números pares del 1 al 100
##Usa un bucle para sumar solo los números pares.
suma = 0

for i in range(1, 100):
    if i % 2 == 0:
        suma += i

print(suma)
    

#Adivina el número
#
#Genera un número aleatorio entre 1 y 10, y deja que el usuario adivine.
#
import random
numero_aleatorio = random.randint(1, 10)  # Incluye tanto el 1 como el 10


numero=int(input("Introduce un numero de 1 al 10: "))

if numero_aleatorio == numero:
    print("Los numeros son iguales")
else:
    print("numeros Distinto numero aleatorio: ",numero_aleatorio, "Numero insertado: ", numero)


#Tabla de multiplicar
#
#Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10.
#

numero1 = int(input("Ingresa un numero: "))
contador =0
while contador<= 10:
    print("la multiplicacion de ", contador,"por el numero", numero1,"es: ", contador*numero1)
    contador +=1


#Lista de nombres
#
#Pide 5 nombres al usuario y guárdalos en una lista. Luego imprímelos.
#

nombres =[]

for i in range(5):
    nombre= input(f"Ingresa el nombre{i + 1}: ")
    nombres.append(nombre)

print("\nLos nombres ingresados son:")
for nombre in nombres:
    print(nombre)
    
#Pide al usuario que ingrese las edades de 5 personas, guárdalas en una lista y luego muestra:
#
#Todas las edades ingresadas.
#
#La edad mayor.
#
#La edad menor.
#
#El promedio de las edades.

edades =[]

for i in range(5):
    edad= int(input(f"Ingresa la edad {i + 1}: "))
    edades.append(edad)

print("\nLos nombres ingresados son:")
for edad in edades:
    print(edad)
    
print("\nLa edad mayor:", max(edades))

print("\nLa edad menor:", min(edades))
print("\nLa edad promedio:", sum(edades)/len(edades))

#Números primos
#
#Pide un número y determina si es primo.

numero_primo= int(input("ingresa un numero primo: "))


# Caso especial para números menores que 2
if numero_primo < 2:
    print(f"{numero_primo} no es un número primo.")
else:
    es_primo = True
    for i in range(2, numero_primo):
        if numero_primo % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"{numero_primo} es un número primo.")
    else:
        print(f"{numero_primo} no es un número primo.")

     
