class Area:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return self.base * self.altura
    
base1 = int(input('Ingrese el base:'))
altura1 = int(input('Ingrese el altura:'))

area1 = Area(base1,altura1)

print(f'El area a calcular es: {area1.calcularArea()}')
    