#Hola, mundo
#
#Imprime en pantalla el texto: "Hola, mundo".
#

print("hola Mundo")


#Suma de dos números
#
#Pide al usuario dos números y muestra su suma.
#

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
suma = n1 + n2
print("La suma de", n1, "y", n2, "es:", suma)

#Número par o impar
#
#Pide un número al usuario e indica si es par o impar.
#
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par.")

#Área de un triángulo
#
#Pide la base y la altura, y calcula el área de un triángulo.

base= int(input("Base del Tiraungulo: "))
altura= int(input("Altura del triangulo: "))

area= base * altura/2

print("La altura del trinagulo es :",area)


#
#Conversión de grados Celsius a Fahrenheit
#
#Usa la fórmula: F = C * 1.8 + 32.
#


temp= int(input("Ingresa la temperatura en Celsius: "))

temp2 = temp * 1.8 + 32

print("La temperatura en grados Fahrenheit es: ",temp2)


#Calculadora básica
#
#Pide dos números y una operación (+, -, *, /) y muestra el resultado.

numero1 = int(input("Ingresa el primer valor: "))
numero2 = int(input("Ingresa el segundo valor: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2


print("El resultado de la suma es: ", suma)
print("El resultado de la resta es: ", resta)
print("El resultado de la multiplicacion es: ", multiplicacion)
print("El resultado de la division es: ", division)
