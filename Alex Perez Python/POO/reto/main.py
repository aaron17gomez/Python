from figura import Rectangulo, Circulo, probar_figura

def main():
    while True:
        menu = """
        AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
        1- Rectangulo
        2- Circulo
        3- Salir
        Ingrese una opcion: """
        opcion = input(menu)
        if opcion == '1':
            base = float(input('Ingrese la Base: '))
            altura = float(input('Ingrese la Altura: '))
            r = Rectangulo(base, altura)
            probar_figura(r)
        elif opcion == '2':
            radio = float(input('Ingrese el Radio: '))
            c = Circulo(radio)
            probar_figura(c)
        elif opcion == '3':
            print('Cerrando sistema!!!!!!')
            break
        else:
            print('Opcion incorrecta')
        
        

if __name__ == '__main__':
    main()

    