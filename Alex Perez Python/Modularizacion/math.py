import math as m

#realizando redondeos con funcion floor
print('Redondeo hacia abajo')
print(m.floor(4.99), '\n')#redondeo hacia la izquierda
print('Redondep hacia arriba')
print(m.ceil(4.99), '\n')#redondeo hacia la derecha

n = [0.99, 1, 2, 3, 4]
print('Suma de los elementos de una lista')
print(m.fsum(n), '\n')#suma los elementos de la lista

#trunqueamientos
print('Elimina los decimales de 45.7567')
print(m.trunc(45.7567), '\n')#despues del decimal los elimina
#potencia
print('Potencia de 2^3')
print(m.pow(2,3), '\n')#dos elevad a la tres
#raiz cuadrada
print('Raiz cuadrada de 16')
print(m.sqrt(16), '\n')
#constantes del modulo
print('Cuanto vale el numero PI')
print(m.pi, '\n')
print('Cuanto vale el numero de Euler')
print(m.e)

