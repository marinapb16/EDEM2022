#RETO 2
#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

num_inicial = int(input("introduce un número inicial: "))
num_final = int(input("introduce número final: "))

if num_inicial %2 == 0 and num_final == 0:
  ListaNumeros = range(num_inicial+1, num_final, 2)
elif num_inicial %2 != 0 and num_final == 0:
  ListaNumeros = range(num_inicial, num_final, 2)
elif num_inicial %2 == 0 and num_final != 0:
  ListaNumeros = range(num_inicial+1, num_final+1, 2)
else:
  ListaNumeros = range(num_inicial, num_final+1, 2)

print(*ListaNumeros)