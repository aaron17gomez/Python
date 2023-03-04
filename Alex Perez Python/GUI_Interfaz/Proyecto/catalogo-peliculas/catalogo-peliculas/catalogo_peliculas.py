#modulo principal
import tkinter as tk #importando nuestra interfaz
from client.gui_app import Frame, barra_menu


def main():
    #raiz o ruta con la clase TK()
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    root.iconbitmap('img/cp-logo.ico')
    root.resizable(0,0)#sea falso como arriba y abajo (0,1) (1,0)
    
    
    
    barra_menu(root)
    
    app = Frame(root = root)
    
    """
    #frame es un contenedor de los elementos a crear
    #creando un frame que contiene los elementos
    frame = tk.Frame(root)
    #la ventana toma el tamaño del frame
    frame.pack()#empaquetando
    frame.config(width = 480, height=320, bg = 'green')#el ancho y el alto
    """
    
    app.mainloop()
    #root.mainloop() #final de la ejecucion de la aplicacion

if __name__ == '__main__':
    main()

