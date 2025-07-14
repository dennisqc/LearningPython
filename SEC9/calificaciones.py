calificaciones=[]

numero_calificaciones = int(input('Proporciona el numero de calificaciones a evaluar:  '))

for indice in range(numero_calificaciones):
    calificacion = int(input(f'Ingresa la calificaciones numero {indice +1}: '))
    calificaciones.append(calificacion)

print(f'Las calificaciones proporcionadas son {calificaciones}')


promedio=sum(calificaciones)/len(calificaciones)

print(f'Promedio de las calificiaciones : {promedio:.2f}')