print('istema de admin')

salir = False

while not salir:
    print(f'''MEnu:
          
          1. Crear Cuenta
          2. Eliminar Cuenta
          3. Salir
          ''')
    opcion = int(input("Escoje una opcion: "))
    if opcion == 1:
        print('Creando tu cuenta... ')
    elif opcion == 2:
        print('Eliminando tu cuenta... ')
    elif opcion == 3:
        print('Saliendo del Sistema... ')
        salir = True

    else:
        print('Ingrea otra opcion')
else: 
    print('Saliendo del sistema')

    ## cajero

