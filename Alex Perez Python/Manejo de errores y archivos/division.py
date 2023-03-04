divi = 0
try:
    a = int(input('Ingrese el Dividendo: '))
    b = int(input('Ingrese el divisor: '))
    
    divi = a / b
except ValueError:
    print('Error: Ingrese solo numeros enteros!')
except ZeroDivisionError:
    print('La division con cero no esta definida!')
except Exception as error:
    print('Ha ocurrido un error no previsto: ', type(error).__name__)
print('La division es:', divi)