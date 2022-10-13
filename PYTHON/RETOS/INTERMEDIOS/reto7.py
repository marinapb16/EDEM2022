#RETO 7
#Escribe un programa que pida 5 precios al usuario y los almacene en una lista de precios. 
# Al finalizar, deberá mostrar por consola la media de los precios introducidos.

precio1 = float(input('Introduce un precio: '))
precio2 = float(input('Introduce otro precio: '))
precio3 = float(input('Introduce otro precio: '))
precio4 = float(input('Introduce otro precio: '))
precio5 = float(input('Introduce otro precio: '))

ListaPrecios = [precio1, precio2, precio3, precio4, precio5]

print(*ListaPrecios)

from numpy import mean
mediaprecios = mean(ListaPrecios)
print(mediaprecios)
