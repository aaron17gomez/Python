from datetime import datetime as d

#informacion actual
print('Tiempo actual')
print(d.now(), '\n')

dt =d.now()
print('Año:', dt.year)
print('Mes:', dt.month)
print('Dia:', dt.day)
print('Hora:', dt.hour)
print('Minutos:', dt.minute)
print('Segundos:', dt.second)

print(f'Fecha: {dt.day}/{dt.month}/{dt.year}')
print(f'Hora: {dt.hour} : {dt.minute} : {dt.second}')


