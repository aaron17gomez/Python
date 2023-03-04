#import fibonacci  #importacion simpre
#fibonacci.fibo(100)
#print(fibonacci.fibo2(100))

#////////////////////////////////////////
#para importar una funcion o clase en espesifico ya sea una o varias funciones
#from fibonacci import fibo, fibo2
#fibo(100)
#print(fibo2(100))

#//////////////////////////////////////////
#con * estamos importando todo lo que tiene el archivo de modulos
#from fibonacci import *
#fibo(100)
#print(fibo2(100))

#//////////////////////////////////////////
#la instruccion "as" es un alias para importar nombres mas complejos o dificil de recordar
#import fibonacci as f
#f.fibo(100)
#print(f.fibo2(100))

#//////////////////////////////////////////
#la instruccion "as" es un alias para importar nombres mas complejos o dificil de recordar 
#from fibonacci import fibo as f1
#from fibonacci import fibo2 as f2

#f1(100)
#print(f2(100))


#----------------------------------------------------------
import sys
import builtins

#con la funcion dir estamos pidiendo informacion del modulo sobre funciones entre otras cosas
#print(dir(sys))
print(dir(builtins))
