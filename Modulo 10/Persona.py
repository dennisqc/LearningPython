class Persona:
    def __init__(self, nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')



persona1 = Persona('Juan','Perez',28)
persona1.mostrarDetalle()
persona1.telefono = '984757093'


persona2 = Persona('Karla','Gomez',78)
persona2.mostrarDetalle()
