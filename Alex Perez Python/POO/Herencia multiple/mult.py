class A:
    def __init__(self):
        print('Soy clase A')
    
    def a(self):
        print('Soy metodo de A')

class B:
    def __init__(self):
        print('Soy clase B')
    
    def b(self):
        print('Soy metodo de B')


#se le da importancia a de la izquierda en este caso a la clase A
class C(A, B):
    def c(self):
        print('Soy metodo de C')