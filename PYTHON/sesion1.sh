#CLASE 17/09

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
VARIABLES

Tipos de variables:

bool - booleanos
int - números enteros
float - números decimales
str - cadenas de texto
list [ ... ]
tuple ( ..., ..., ... )
dic { key: value, key: value ... }
set
range - rangos
complex - complejos
frozenset - set que no puede variar, está congelado
bytes - para representar en bytes los valores


En python declaramos variables y le asignamos valor de la siguente manera:

nombre_variable: tipo de dato = valor asignado

'''

'''
STR - cadenas de texto
las cadenas de texto se limitan con comillas, pueden ser comillas simples o dobles.
'''
miCadena1:str = 'Hola mundo'
miCadena2:str = "Hola mundo"

'''
INT- números enteros
'''
miEdad:int = 23

'''
FLOAT - números decimales
'''
temperatura:float = 19.5

'''
BOOL - cómo documentamos valores booleanos
'''
casado: bool = True
print(f"Casado? {casado}")

con_hijos: bool = False

'''
DIC - diccionarios
Sirven para almacenar datos en forma de clave-valor
'''
miDiccionario = dict()

miDiccionario = {
  "name" : "Marina",
  "age" : 23,
  "dni" : "12345H"
}

'''
TUPLAS
son estáticas y no pueden cambiar su tamaño
'''
miTupla = (5, "Hola mundo!", True, -4.5)


'''
LISTAS (vamos a trabajar mucho con ellas en el mundo datos)
'''
miLista: [str] = ["Martín", "Juan", "Pablo"]

print(miLista)
print(*miLista)

print(miLista[1]) #imprimo el segundo valor de la lista
#¡OJO!: en el mundo de la informática se empieza a contar a partir del 0

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

'''
SETS
Un set es una colección que no posee órden, y por tanto, tampoco números de índex. Esto quiere decir que no podemos decidir el orden en el cual aparecerán sus elementos
'''

misNumeros = [1,4,6,3,2,6,4,7,9,4,2,8,0,2,6,5,5,5,5]
print(set(misNumeros))

miOtroSetDeDatos = set(["a", "a", "a", "a", "a", "b"])
print(*miOtroSetDeDatos)

'''
SORT - para ordenar listas
REVERSE - invierte lista

Una diferencia clave entre sort() y sorted(), es que sorted() retornará una nueva lista, mientras que sort() ordena la lista en su lugar
'''

ListaNumeros = [1,4,7,9,3,5,6,]

ListaNumeros.sort()


#Ejemplo

name = input("Hola, dime tu nombre: ")
edad = int(input("¿Cuál es tu edad? "))

print(f"Hola {name}. Tienes {edad} años")


#Ejercicio de consola
#nombre, email, contraseña, edad, aceptar
#cuando tengamos todos los datos creamos un diccionario llamado usuario y mostramos diccionario por pantalla

name = input("Hola, dime tu nombre: ")
edad = int(input("¿Cuál es tu edad? "))
email = input("Introduce tu correo electrónico: ")
contraseña = input('Introduce la contraseña: ')

Usuario = dict()

Usuario = {
  "nombre" = name
  "edad" = edad
  "email" = email
  "contraseña" = contraseña
}
print(Usuario)