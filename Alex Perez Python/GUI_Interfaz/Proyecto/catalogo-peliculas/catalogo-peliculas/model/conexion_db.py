#SQL crea un archivo que no necesita de un servidor si no que se creamos un archivo para conectarnos

import sqlite3

class ConexionDB:
    #abriendo la conexion
    def __init__(self):
        #crea o busca la BD en la carpeta database
        
        self.base_datos = 'database/peliculas.db'
        
        #atributo que realiza la concexion obtendra la conexion
        self.conexion = sqlite3.connect(self.base_datos)
        
        #creando un atributo cursor
        #el cursor ejecutara el cursor dentro de l BD
        self.cursor = self.conexion.cursor()
    
    #cerrando la conexion
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()