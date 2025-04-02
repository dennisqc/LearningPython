cadena1 = 'Hola'
cadena2 = 'Mundo'

concatenacion = cadena1 + ' ' + cadena2

concatenacion2 = ''.join([cadena1, ' ', cadena2])
print(concatenacion)
print(concatenacion2)

#formateo de cadenas    

nombre = 'Laura'
edad = 26

mensaje = f'Hola, mi nombre es {nombre} y tengo {edad} años.'

print(mensaje)

cadena = 'Hola Mundo'
largo_cadena = len(cadena)

print(f'La longitud de la cadena es: {largo_cadena}')

nombre_completo = 'Laura Martinez'
nombre, apellido = nombre_completo.split()
print(f'Nombre: {nombre}')
print(f'Apellido: {apellido}')

nombre_usuario=nombre_completo.strip()
nombre_usuario = nombre_usuario.replace(' ', '.')
nombre_usuario = nombre_usuario.lower()
print(f'Nombre de usuario: {nombre_usuario}')