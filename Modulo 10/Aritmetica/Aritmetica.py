class Aritmetica:
    
    """
    Clase aritmetica para realizare las operaciones de sumar, restar, etc.
    """
    def __init__(self,operandoA,OperandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = OperandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
aritmetica1 = Aritmetica(8,1)

print(aritmetica1.sumar())

print(aritmetica1.restar())