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
    
    
    
    
while True:
    print("📱 Agenda de Contactos")
    
    opcion = input("Selecciona una opción (1-5): ").strip()
    
    if opcion == "1":
        agregar_contacto()