def sumar(n1, n2):
    suma = n1 + n2
    print('La suma es:', suma)

def area(n1, n2):
    area = n1 * n2
    perimetro = 2*(n1 + n2)
    print('El area es:', area)
    print('El perimetro es:', perimetro)

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
sumar(n1, n2)
area(n1, n2)

print('area es de tipo:',type(area))