import math
#usando if
valor1=150
valor2=2
result = valor1-valor2
if result < 0 :
    print('El resultado es negativo')
elif result>100:
    print('El resultado se encuentra fuera de rango')
else:
    print(result)

#bucle o ciclo while() realiza una repeticion de acciones mientras se cumpla con una condicion explicitada
b=1
obtener = 0
while b <= 10:
    obtener = obtener + b
    b = b + 1
    print(obtener)


print('')
numero = int(input('Digite su numero: '))

while numero<0:
    print('Error -> Escriba un numero positivo')
    numero = int(input('Digite un numero: '))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")

i = 0
while i<10:
    print('{i} Hola mundo')
    i += 1

#suma de dos numeros
var1 = int(input("Escriba su numero: "))
var2 = int(input("Escriba otro numero: "))
suma = var1 + var2
print("La suma de",var1,"+",var2,"=",suma)

#valor mayor de los dos numeros
if (var1 > var2):
    mayor = var1
    menor =var2
elif (var1 == var2):
    print("El numero", var1, "es igual a", var2)
else:
    mayor = var2
    menor = var1
    print("el numero", mayor, "es mayor que", menor)
    print("el numero", menor, "es menor que", mayor)

#interaccion con el usuario
nombre = input("Ingrese su nombre: ")
print("Bienvenido", nombre)

#obteniendo los numeros del 1-100
for i in range(1,101):
    print(i)
    
#obteniendo los numeros del 1-100 con while
i = 1
print("-----------Begin----------------")
while (i<= 100):
    print(i)
    i+=1
print("------------End----------------")

#calculando los numeros pares del 1-100
print("----------Forma 1----------------")
for i in range(1, 101):
    if((i % 2) == 0):
        print(i)
print("------------End----------------")


print("-----------Begin----------------")
for i in range(2, 11, 2):
    print(i)
print("------------End----------------")

#palindromo cuando dos palabras son iguales al reves y derecho
cadena = input("ingrese una palabra: ")
reversa = cadena[::-1]
if (cadena == reversa):
    print("Es palindromo", cadena, "es igual a", reversa)
else:
    print("No es palindromo", cadena, "es diferente que", reversa)
    
#numero a encontrar con la libreria random
import random
def generar_num_aleatorio (minimo, maximo):
    return random.randint(minimo, maximo)
numero_buscado = generar_num_aleatorio(1, 100)
encontrado = False
intentos = 0
#print(numero_buscado)

while not encontrado:
    numero_usuario = int(input("Ingrese el numero buscado: "))
    if numero_usuario > numero_buscado :
        print("El numero que busca es menor")
        intentos +=1
    elif numero_usuario < numero_buscado :
        print("El numero que busca es mayor")
        intentos +=1
    else :
        encontrado = True
        print("El numero es correcto",numero_usuario,"tus intentos fueron:",intentos,"intentos" )

        #excepciones
while True:
    try:
        val_num1 = int(input("Ingrese su numero: "))
        break
    except ValueError :
        print("Ingrese un numero.")

while True:
    try:
        val_num2 = int(input("Ingrese su numero: "))
        break
    except ValueError :
        print("Ingrese un numero.")

suma = val_num1 + val_num2
print("la suma de los dos numeros es:", val_num1, "+",val_num2, "=", suma)
