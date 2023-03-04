class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def detalle_persona(self):
        print(f'Nombre: {self.nombre} \nEdad: {self.edad}')
    
    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'
    

#creando una subclase
#en ves de solo colocar dos puntos ponemos parentecis y agregamos la clase padre Persona
#se hereda todo lo de la clase padre
class Cliente(Persona):
    pass

#Clase empleado que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        #usando funcion super para referirse a la clase padre
        #esta heredando el constructor de la clase padre
        #super().__init__(nombre, edad)
        Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo
        
    
    def detalle_empleado(self):
        #super().detalle_persona()
        Persona.detalle_persona(self)
        print('Sueldo:', self.sueldo)
    
    def __str__(self):
        #return super().__str__() + f'\nSueldo: {self.sueldo}'
        return Persona.__str__(self) + f'\nSueldo: {self.sueldo}'
        