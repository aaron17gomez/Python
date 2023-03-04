#interfaz de ususario
import tkinter as tk
from tkinter import ttk
from model.pelicula_dao import crear_tabla, borrar_tabla

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)#anclando nuestra barra de menu
    
    #creando el menu de inicio como objeto
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(labe = 'Inicio', menu = menu_inicio)
    
    menu_inicio.add_command(label = 'Crear Registro en la BD', command= crear_tabla)
    menu_inicio.add_command(label = 'Eliminar Registro en BD', command= borrar_tabla)
    menu_inicio.add_command(label = 'Salir', command = root.destroy)#destroy cierra el programa
    
    #creando mas botones al menu
    barra_menu.add_cascade(labe = 'Consultas')
    barra_menu.add_cascade(labe = 'Configuracion')
    barra_menu.add_cascade(labe = 'Ayuda')




#clase padre hereda de mi propia clase frame
class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width = 480, height=320 )
        self.root = root
        #como estoy heredando de frame paso a empaquetar
        self.pack()
        
        # self.config(bg = 'green')
        
        self.campos_pelicua()
        self.desabilitar_campos()
        self.tabla_pelicula()
    
    
    def campos_pelicua(self):
        
        ######################Label########################
        self.label_nombre = tk.Label(self, text ='Nombre: ')
        self.label_nombre.config(font = ('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        
        self.label_duracion = tk.Label(self, text ='Duracion: ')
        self.label_duracion.config(font = ('Arial', 12, 'bold'))
        self.label_duracion.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        
        self.label_genero = tk.Label(self, text ='Genero: ')
        self.label_genero.config(font = ('Arial', 12, 'bold'))
        self.label_genero.grid(row = 2, column = 0, padx = 10,pady = 10)
        
        ###############Campos de etradas###################
        #entrys campos de entrada
        
        #creando objeto mi_nombre de la clase stringvar
        #el stringVar permite recoger datos y enviar datos a estos campos o sea los entires
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width = 50, font = ('Arial', 12))
        self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan= 2)# con columnspan hacemos que los entries esten en dos columnas
        
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable = self.mi_duracion)
        self.entry_duracion.config(width = 50, font = ('Arial', 12))
        self.entry_duracion.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan= 2)
        
        
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable = self.mi_genero)
        self.entry_genero.config(width = 50, font = ('Arial', 12))
        self.entry_genero.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan= 2) 
        
        #####################Botones#####################
        self.boton_nuevo = tk.Button(self, text = 'Nuevo', command= self.habilitar_campos)
        self.boton_nuevo.config(width = 20, font = ('Arial', 12, 'bold'), fg = '#DAD5D6', bg = '#158645', cursor = 'hand2', activebackground = '#35BD6F')
        self.boton_nuevo.grid(row = 3, column= 0,  padx = 10, pady = 10)
        
        
        self.boton_guardar = tk.Button(self, text = 'Guardar', command= self.guardar_datos)
        self.boton_guardar.config(width = 20, font = ('Arial', 12, 'bold'), fg = '#DAD5D6', bg = '#1B98F4', cursor = 'hand2', activebackground = '#34A4F6')
        self.boton_guardar.grid(row = 3, column= 1,  padx = 10, pady = 10)
        
        
        self.boton_cancelar = tk.Button(self, text = 'Cancelar', command= self.desabilitar_campos)
        self.boton_cancelar.config(width = 20, font = ('Arial', 12, 'bold'), fg = '#DAD5D6', bg = '#ED332B', cursor = 'hand2', activebackground = '#EF544E')
        self.boton_cancelar.grid(row = 3, column= 2,  padx = 10, pady = 10)
        
    #metodo de habilitar los campos
    def habilitar_campos(self):
        #creando campos vacios o sea vaciando los campos
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        self.entry_nombre.config(state= 'normal')
        self.entry_duracion.config(state= 'normal')
        self.entry_genero.config(state= 'normal')
            
        self.boton_guardar.config(state= 'normal')
        self.boton_cancelar.config(state= 'normal')    
    
    
    
    #metodo de habilitar los campos    
    def desabilitar_campos(self):
        #creando campos vacios
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        
        self.entry_nombre.config(state= 'disabled')
        self.entry_duracion.config(state= 'disabled')
        self.entry_genero.config(state= 'disabled')
            
        self.boton_guardar.config(state= 'disabled')
        self.boton_cancelar.config(state= 'disabled')
        
    def guardar_datos(self):
        self.desabilitar_campos()  
        
    def tabla_pelicula(self):
        self.tabla = ttk.Treeview(self, column =('Nombre', 'Duracion', 'Genero'))
        #en que parte va estar nuestra tabla
        self.tabla.grid(row = 4, column = 0, columnspan = 4)
        
        #encabbezado
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#0', text='GENERO')
        
        #insertando datos
        self.tabla.insert('', 0, text= '1', values= ('Los vengadores', '2.35', 'Accion'))
        
        #BOTONES
        #boton editar
        self.boton_editar = tk.Button(self, text = 'Editar')
        self.boton_editar.config(width = 20, font = ('Arial', 12, 'bold'), fg = '#DAD5D6', bg = '#158645', cursor = 'hand2', activebackground = '#35BD6F')
        self.boton_editar.grid(row = 5, column= 0,  padx = 10, pady = 10)
        
        #boton eliminar
        self.boton_eliminar = tk.Button(self, text = 'Eliminar')
        self.boton_eliminar.config(width = 20, font = ('Arial', 12, 'bold'), fg = '#DAD5D6', bg = '#ED332B', cursor = 'hand2', activebackground = '#EF544E')
        self.boton_eliminar.grid(row = 5, column= 1,  padx = 10, pady = 10)
        
        
          
        
        
    