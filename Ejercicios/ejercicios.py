#Dado un diccionario con nombres de empleados y sus salarios en dólares, escribe una función que transforme los valores a euros. Usa un tipo de cambio de **1 USD = 0.92 EUR**

def convertir_salarios_a_euros(employes,tipodecambio=0.92):
    empleados_euros = {}
    for nombre, salario_usd in employes.items():
        salario_eur = salario_usd * tipodecambio
        empleados_euros[nombre] = salario_eur
    return empleados_euros


employees = {"Ana": 5000, "Luis": 4500, "Carlos": 6000}
empleados_euros = convertir_salarios_a_euros(employees)
print(empleados_euros)