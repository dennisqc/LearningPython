#1. Agenda de contactos avanzada
#Crea un programa con un diccionario donde:
#Se puedan agregar contactos con nombre, teléfono y correo.
#Se pueda buscar un contacto por nombre.
#Se pueda eliminar un contacto.
#Usa un menú de opciones con input() y un while.

agenda= {}

def agregar_contacto():
    nombre = input("Ingresa el nombre").strip()
    telefono =input("Ingresa el telefono").strip()
    correo =input("Ingresa el correo").strip()
    
    agenda[nombre] = {
        "telefono":telefono,
        "correo": correo       
    }
    print(f"✅ Contacto '{nombre}' agregado con éxito.\n")

def buscar_contacto():
    nombre = input("Ingresa el nombre: ").strip()
    
    print(f"Nombre: {nombre}")
    print(f"Telefono: {agenda[nombre]['telefono']}")
    print(f"Telefono: {agenda[nombre]['correo']}")

def eliminar_contacto():
    nombre = input("Ingresa el nombre: ").strip()
    
    if nombre in agenda:
        del agenda[nombre]
        
        print(f"Contacto Eliminado {nombre}")
    else:
        print(f"No existe el contacto")

def mostrar_contacto():
    if not agenda:
        print("📭 La agenda está vacía.\n")
        return
    print("\n📒 Contactos en la agenda:")
    for nombre, datos in agenda.items():
        print(f" - {nombre}: {datos['teléfono']} / {datos['correo']}")
    print()

# Menú interactivo
while True:
    print("📱 Agenda de Contactos")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Ver todos los contactos")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ").strip()
    
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        mostrar_contacto()
    elif opcion == "5":
        print("👋 Cerrando la agenda. ¡Hasta luego!")
        break
    else:
        print("⚠️ Opción no válida. Intenta de nuevo.\n")