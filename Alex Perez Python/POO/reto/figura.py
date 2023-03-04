import math

class Fifura:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def area(self):
        pass
    
    def perimetro(self):
        pass


class Rectangulo(Fifura):
    def __init__(self, base, altura):
        #se esta redefiniendo el nombre de esta clase
        #muestra el estado del objeto
        self.nombre = __class__.__name__ #saca el nombre de la clase
        self.base = base
        self.altura = altura
    
    def area(self):
       return self.base * self.altura
    
    def perimetro(self):
        return 2*self.base + 2*self.altura 
    
    def __str__(self):
        return f'{self.nombre}[base:{self.base} altura:{self.altura}]'
        

class Circulo(Fifura):
    def __init__(self, radio):
            #se esta redefiniendo el nombre de esta clase
        #muestra el estado del objeto
        self.nombre = __class__.__name__ #saca el nombre de la clase
        self.radio = radio
    
    def area(self):
       return 2* self.radio
    
    def perimetro(self):
        return 2*math.pi * self.radio 
    
    def __str__(self):
        return f'{self.nombre}[radio:{self.radio}]'

def probar_figura(figura):
    print(figura)
    print('Area:', figura.area())
    print('Perimetro:', figura.perimetro())


#312, 459,475