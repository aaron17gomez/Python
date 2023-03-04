from persona import Cliente, Empleado

#creando un cliente
cliente1 = Cliente('Alex', 25)
cliente = Cliente('Jorge', 26)

#cliente1.detalle_persona()
#print('='*25)
#print(cliente)

empleado1 = Empleado('Marcos', 30, 50000)
empleado2 = Empleado('Lucas', 20, 20000)


empleado1.detalle_persona()
print('='*25)
empleado1.detalle_empleado()
print('='*25)
#estado del empleado
print(empleado2)