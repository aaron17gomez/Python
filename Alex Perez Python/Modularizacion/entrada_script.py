import sys

#print(sys.argv) #retorna una lista
if len(sys.argv) == 3:
    texto = sys.argv[1]
    cantidad = int(sys.argv[2])

    c = 0
    while c < cantidad:
        print(texto)
        c += 1 
else:
    print('Error, Ingrese los argumentos correctamente')
    print('Ejemplo: entrada_script.py "Texto" 5')