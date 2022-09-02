class objeto:
    def __init__(self, ele1, ele2, ele3, ele4, ele5, ele6) -> None:
        self.numComplex1 = complex(ele1, ele2)
        self.numComplex2 = complex(ele3, ele4)
        self.numComplex3 = complex(ele5, ele6)
    
    def show(self):
        print(f"Operações: \n Soma: {self.numComplex1 + self.numComplex2 + self.numComplex3} \n Subtração: {self.numComplex1 - self.numComplex2 - self.numComplex3} \n Multiplicação: {self.numComplex1 * self.numComplex2 * self.numComplex3} \n Divisão: {self.numComplex1 / self.numComplex2 / self.numComplex3}")
        print(f"Primeiro numero real: {self.numComplex1.real}")
        print(f"Primeiro numero imaginario: {self.numComplex1.imag}")
        print(f"Segundo numero real: {self.numComplex2.real}")
        print(f"Segundo numero imaginario: {self.numComplex2.imag}")
        print(f"Terceiro numero real: {self.numComplex3.real}")
        print(f"Terceiro numero Imaginario: {self.numComplex3.imag}")



complexo = objeto(1,2,3,4,5,6)
complexo.show()
