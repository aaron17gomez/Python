from io import open  
from os import path # si el archivo existe o no

#creando una funcion para escribir
def escribir_archivo():
    archivo = open('texto.txt', 'w')# se esta abriendo este archivo para escribir datos
    archivo.write('Hola Mundo de PYTHON')
    archivo.close()

def leer_archivo():
    #estamos leyendo con r y con la librerioa OS y con path nos ayuda a saber si existe o no el archivo
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r')
        #textos = archivo.read()
        textos = archivo.readlines()#nos manda una lista
        archivo.close()
        
        print(textos)
    else:
        print('No existe el archivo')

def agregar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'a')#actualiza datos o agrega datos
        archivo.write('\nHola Roel Ramos')
        archivo.close()
  
    else:
        print('No existe el archivo')  
        
def modificar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r+')#modo lectura y escritura con r+
        texto = archivo.readlines() #creando una lista de lo que esta escrito
        print(texto)
        texto[1] = 'Hola alumnos de programacion\n'
        #archivo.write('\nHola Roel Ramos')
        print(texto)
        #usando puntero para indicar que se va a reinscribir dese el inicio
        archivo.seek(0)
        #actualizar la informacion
        archivo.writelines(texto)
        archivo.close()
        print(texto)
  
    else:
        print('No existe el archivo')  

def eliminar_datos():
    #borra todo porque a a reinscribir
    archivo = open('texto.txt', 'w')# se esta abriendo este archivo para escribir datos
    archivo.close()

#escribir_archivo()
#leer_archivo()
#agregar_datos()
#def modificar_datos()
eliminar_datos()