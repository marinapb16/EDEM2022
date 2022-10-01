# Esto es un comentario
'''Esto es un comentario
especialmente largo'''
print("hola mundo")

user = "Marina"

print("hola", user)

user = "Alba"

print("hola", user)

user = 200

user = user * 2

newuser:str = "Pepe"
newuser = 3

print(newuser)

user = "Juan"
bienvenida = f"Hola {user}"

print(f"¡Hola {user}!")

print(f"{bienvenida} \ntu numero de usuario es {newuser}")




'''
bool 
int - números enteros
float - decimales
str 
list [ ... ]
tuple ( ..., ..., ... )
dic { key: value, key: value ... }
set
range
complex - complejos
frozenset - set que no puede variar, está congelado
bytes - para representar en bytes los valores
'''




'''
BOOL - cómo documentamos valores booleanos
'''
casado: bool = True

print(f"Casado? {casado}")

'''
LISTAS (vamos a trabajar mucho con ellas en el mundo datos)
'''
miLista: [str] = ["Martín", "Juan", "Pablo"]

print(miLista)
print(*miLista)

print(miLista[1])

ListaCompra: [str] = ["huevos", "lechuga", "tomates", "manzanas", "melocotones"]
n = len(ListaCompra)
print(ListaCompra[n-2], ListaCompra[n-1])

#manera más eficiente
print(*ListaCompra[-2:])

'''
RANGOS
'''
miRango = range(0,11,2)
print(*miRango)


#persona = {
  #"name" : "Marina",
  #"age" : 23,
  #"dni" : "12345H"
  #"casado" : True
#}
#print(f'El DNI de {persona["name"]} es {persona["dni"]}')

'''
SETS
'''

misNumeros = [1,4,6,3,2,6,4,7,9,4,2,8,0,2,6,5,5,5,5]
print(set(misNumeros))

miOtroSetDeDatos = set(["a", "a", "a", "a", "a", "b"])
print(*miOtroSetDeDatos)

#sort - para ordenar listas
#reverse - invierte lista
#diferencia sort y sorted??

ListaNumeros = [1,4,7,9,3,5,6,]

ListaNumeros.sort()

#paso por "valor" y paso por "referencia"

name = input("Hola, dime tu nombre: ")
edad = int(input("¿Cuál es tu edad? "))

print(f"Hola {name}. Tienes {edad} años")


#Ejercicio de consola
#nombre, email, contraseña, edad, aceptar
#cuando tengamos todos los datos creamos un diccionario llamado usuario y mostramos diccionario por pantalla
