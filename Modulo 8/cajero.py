saldo = 1000

def deposito():
    global saldo
    x = int(input("Ingrese el monto a depositar: "))
    saldo += x
    print(f"✅ Depósito exitoso. Nuevo saldo: {saldo}\n")

def retirar():
    global saldo
    x = int(input("Ingrese el monto a retirar: "))
    if saldo >= x:
        saldo -= x
        print(f"✅ Se retiró {x}. Nuevo saldo: {saldo}\n")
    else:
        print("❌ El monto a retirar supera el saldo disponible.\n")

def consultar():
    print(f"💰 Saldo actual: {saldo}\n")

while True:
    print("==== 🏦 MENÚ DEL CAJERO ====")
    print("1. Depositar Saldo")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ").strip()
    
    if opcion == "1":
        deposito()
    elif opcion == "2":
        retirar()
    elif opcion == "3":
        consultar()
    elif opcion == "4":
        print("👋 Cerrando el sistema. ¡Hasta luego!")
        break
    else:
        print("⚠️ Opción no válida. Intenta de nuevo.\n")
