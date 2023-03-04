
class Persona:
    #los atributos son las variables y las definimos
    #nombre = None
    #edad = None
    
    #un constructor es el que contruye un objeto
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #los metodos son comportamientos del objeto
    #los metodos se definen como una funcion
    #self es para indicar que este metodo pertenece a la clase persona
    def mostrar_datos(self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)
        
    #creando otro metodo donde devuelve el estado del objeto
    #se mostrara en main al momento que lo llamemos con la funcion print()
    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'
    
    







