#modulo de numeros de fibonacci

def fibo(n):
    a,b = 0, 1
    while a < n:
        print(a, end=' ')
        #secuencia de fibonacci
        #1, 1, 2, 3, 5
        a, b = b, a + b
    print()

def fibo2(n):
    resultado = []
    a,b = 0, 1
    while a < n:
        resultado.append(a)
        #secuencia de fibonacci
        #1, 1, 2, 3, 5
        a, b = b, a + b
    return resultado

