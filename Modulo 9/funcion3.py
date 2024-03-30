# def ListarNombres(*nombres):
#     for nombre in nombres:
#         print(nombre)

# ListarNombres('Juan','Karla','Maria','Ernesto','Dennis')

def SumarValores(*args):
    resultado = 1
    for numeros in args:
        resultado *=  numeros
    return resultado

print(SumarValores(3, 5, 9,4,8,7))
