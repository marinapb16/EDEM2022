#RETO 15
#Escribe una función que reciba una muestra de números en una lista y 
# devuelva otra lista con sus cuadrados.

n1 = int(input('Introduce un número: '))
n2 = int(input('Introduce otro número: '))
n3 = int(input('Introduce otro número: '))
n4 = int(input('Introduce otro número: '))

ListaNumeros: int = [n1, n2, n3, n4]

ListaNumeros = [n1**2, n2**2, n3**2, n4**2]

print(*ListaNumeros)