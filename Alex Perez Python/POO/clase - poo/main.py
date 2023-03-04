from persona import Persona

#instancia y esta variable que se le asigna la clase se convierte el objeto
persona1 = Persona('Jorge', 25)
#modificando
persona1.nombre = 'Marcos'
""""
persona1.nombre = 'Alex'
persona1.edad = 26
persona2 = Persona()
persona2.nombre = 'Jose'
persona2.edad = 20
"""

persona1.mostrar_datos()
print('='*25)
print(persona1)
#persona2.mostrar_datos()