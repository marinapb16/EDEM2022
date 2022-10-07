#CLASE 22/09


'''
PALABRAS RESERVADAS DE PYTHON
(se ponen de color azul al escribirlas en este editor de texto)

- and
- as
- assert
- break : romper el código en cierto momento
- class : reservada para declarar tipos propios
- continue
- def
- del
- elif
- else
- except
- exec
- finally 
- for 
- global
- if
- import
- in : dentro de algo que sea iterable 
- is : para saber de que tipo son los valores, que condiciones cumplen
- lambda
- nonlocal
- not : negación
- or : se tiene que cumplir una condición o otra
- pass : para saltar alguna iteración, permite continuar
- raise
- return
- try
- while : se ejecuta siempre y cuando la condición se cumple, hay que poner condición para que termine el bucle
- with
- yield
- True
- False
- none

'''

'''
OPERADORES
Los operadores son símbolos, signos o palabras que el intérprete o compilador puede identificar como parte de su sintaxis para llevr a cabo una acción u operación

Operadores numéricos:
-Suma: +
-Resta: -
-Multiplicación: *
-División: /
-División entera: //
-Exponente: **
-Módulo(resto): %
'''

a: int = 1
b: int = 2

#EJEMPLO SUMA
suma: int = a + b
print(f"> Suma 1 + 2 = {suma}")

#EJEMPLO RESTA
resta: int = a - b
print(f"> Resta 1 - 2 = {resta}")

#EJEMPLO MULTIPLICACIÓN
multiplicacion: int = a * b
print(f"> Multiplicación 1 * 2 = {multiplicacion}")

#EJEMPLO DIVISIÓN
division: float = a / b
print(f"> Division 1 / 2 = {division}")

#EJEMPLO DIVISIÓN ENTERA
division_entera: float = a // b
print(f"> Division Entera 1 // 2 = {division_entera}")

#EJEMPLO EXPONENTE
potencia: float = a ** b
print(f"> Potencia 1 ** 2 = {potencia}")

#EJEMPLO RESTO
resto: float = a % b
print(f"> Resto 1 % 2 = {resto}")

'''orden en que se realizan las operaciones:
1. Paréntesis
2. Exponente
3. Multiplicación
4. División
5. Suma
6. Sustracción
'''
#Ejemplos:
operacion_compleja = 33 * 10 + 2 / 5 ** 2
print(f"> Operación 33*10+2/5**2 = {operacion_compleja}")

operacion_compleja_2 = (33 * 10) + (2 / (5 ** 2))
print(f"> Operación (33*10)+(2/(5**2)) = {operacion_compleja_2}")

'''
Operadores de texto:
Son operadores pensados para realizar acciones sobre las cadenas de texto:
-Concatenación: +
-Repetición: *
'''
nombre: str = "Martín"
apellidos: str = "San José de Vicente" 

# Concatenación
nombre_completo: str = nombre + " " + apellidos
print(f"> Nombre completo: {nombre_completo}")  

# Repetición
nombre_x5: str = nombre*5
print(f"> Nombre 5 veces: {nombre_x5}")

'''Operadores de comparación:
-Igualdad: == y tambiñes is (operador de identidad positivo)
-Distinción: != y también is not (operador de identidad negativa)
-Mayor que: >
-Mayor o igual: >=
-Menor que: <
-Menor o igual: <=
'''
#EJEMPLOS:

c: int = 3
d: int = 3
e: int = 4

#Ejemplo igualdad

# Nos devolverá True o False
print(f"> ¿3 y 3 son iguales? {c is d}") #Operador Identidad
print(f"> ¿3 y 3 son iguales? {c == d}")
print(f"> ¿3 y 4 son iguales? {c is e}") #Operador Identidad

#Ejemplo desigualdad

print(f"> ¿3 y 3 no son iguales? {c is not d}")#Operador identidad
print(f"> ¿3 y 4 no son iguales? {c is not e}")#Operador identidad
print(f"> ¿3 y 3 no son iguales? {c != d}")

#Ejemplo de mayor que/mayor igual que:

print(f"¿3 mayor que 2? {3 > 2}")
print(f"¿2 mayor que 3? {2 > 3}")
print(f"¿3 mayor o igual que 3? {3 >= 3}")

#Ejemplo de menor que/menor igual que:

print(f"> ¿2 menor que 3? {2 < 3}")
print(f"> ¿3 menor que 2? {3 < 2}")
print(f"> ¿3 menor o igual que 3? {3 <= 2}")

'''
Operadores lógicos:
-Y (esto Y esto): AND
-Ó (esto ó esto): OR
-lo contrario: NOT
'''
#Ejemplo AND
print(f"> Verdadero y Verdadero = {True and True}")
print(f"> Verdadero y Falso = {True and False}")
print(f"> Verdadero y 1 = {True and 1}")
print(f"> Falso y Falso = {False and False}")
print(f"> Falso y 0 = {False and 0}")
print(f"> Falso y None = {False and None}")

#Ejemplo OR
print(f"> Verdadero o Verdadero = {True or True}")
print(f"> Verdadero o Falso = {True or False}")
print(f"> Falso o False = {False or False}")

#Ejemplo NOT
print(f"> Not Verdadero = {not True}")
print(f"> Not Falso = {not False}")
print(f"> Not Falso o Verdadero = {not (False or True)}")

'''
Operadores de pertenencia:
-Si un valor contiene otro: IN
-Si un valor no contiene otro: NOT IN
'''
#Ejemplo
mi_texto:str = "Lorem ipsum dolor sit amet consectetur adipiscing elit dui odio"
mi_sub_texto: str = "amet"
mi_otro_sub_texto: str = "pepito"

#Pertenece
print(f"> ¿amet está dentro del mi_texto?: {mi_sub_texto in mi_texto}")

#NO pertenece
print(f"> ¿pepito no está dentro de mi_texto?: {mi_otro_sub_texto not in mi_texto}")

'''
Operadores de asignación:
-Asignación simple: =
-Asignación con suma: +=
-Asignación con resta: -=
-Asignación con multiplicación: *=
-Asignación con división: /=
-Asignación con división entera: //=
-Asignación con exponente: **=
-Asignación con resto: %=
'''
#Asignación simple
puntos_obtenidos: int = 0
print(f"> Los puntos obtenidos actuales son: {puntos_obtenidos}")
#Asignación suma
puntos_obtenidos = puntos_obtenidos + 1
print(f"> Los puntos obtenidos actuales son: {puntos_obtenidos}")

puntos_obtenidos += 1
print(f"> Has conseguido otro punto. Ahora tienes: {puntos_obtenidos}")

#Asignación Resta
puntos_obtenidos = puntos_obtenidos - 3
print(f"> Has perdido 3 puntos. Ahora tienes: {puntos_obtenidos}")

puntos_obtenidos -= 3
print(f"> Has perdido 3 puntos. Ahora tienes: {puntos_obtenidos}")


# Multiplicación
puntos_obtenidos = puntos_obtenidos * 2
print(f"> Enhorabuena, tus puntos se multiplican por 2. Ahora tienes: {puntos_obtenidos}")

puntos_obtenidos *= 2
print(f"> Enhorabuena, tus puntos se multiplican por 2. Ahora tienes: {puntos_obtenidos}")

'''
Operadores de bits:
-NOT: not
-AND: &
-OR: |
-XOR: ^
'''