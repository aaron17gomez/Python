class Persona:
    #atributos privados y se pueden usar detro de la clase y no afuera
    #con doble barra abaja son atributos privados
    #se esta encapsulando
    __nombre = None
    __edad = None
    
    #constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    
    def __metodo_privado(self):
        print('Soy un metodo privado')
        
    #encapsulamiento
    #______________________________________________
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edafa(self, edad):
        self.__edad = edad
    #_______________________________________________
    
    #metodo
    def __str__(self):
        return f'Nombre: {self.__nombre} \nEdad: {self.__edad}'
    