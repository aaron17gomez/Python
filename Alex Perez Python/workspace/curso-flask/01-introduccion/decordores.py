def decorador(func):
    
    def decorar(*arg):
        print('Iniciar la ejecucion de la funcion:', func.__name__)
        
        func(*arg)
        print('Terminar la ejecucion de la funcion:', func.__name__)
    
    return decorar
        
#decorando funciones
@decorador #envio de la funcion de arriba a la duncion hola
def hola(nombre):
    print('Hola', nombre)

@decorador
def sumar(a, b):
    suma = a + b
    print('La suma es:', suma)
 
hola('Jorge')
sumar(5, 25)