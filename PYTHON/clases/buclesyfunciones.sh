#CLASE 23/09

'''
CONDICIONALES
-IF
-ELSE IF
-ELSE
Sirven para controlar el flujo de ejecución a partir de una condición. Es decir, ejecutar algo o no ejecutarlo dependiendo de alguna condición.

En Python, la estructura es con "elif" y no con "else if"
'''

#EJEMPLO
miEdad = 45
if (miEdad >= 60):    
  print('Apuntarse al gym')
elif (miEdad < 60 and miEdad > 30):    
  print ('Adulto maduro')
elif (miEdad == 30):    
  print ('Adulto en su sweet moment')
elif (miEdad < 30 and miEdad >= 18):    
  print ('Adulto joven, todo en orden')
else:    
  print ('¡A clase!')

'''
BUCLES
Consisten en realizar una iteración hasta que se cumpla alguna condición que marquemos
'''

'''
FOR
Consiste en realizar una tarea tantas veces como se indique en la condición que se establezca
'''
#Ejemplo1
listaCompra = ['agua', 'cafe', 'cerveza']

for producto in listaCompra:
  print('f{producto}')

#la primera vez que ejecutemos nos sale 'agua', la segunda saldrá 'café' y la tercera 'cerveza'

#Ejemplo2
lista = [1,2,3,4,5,6,7,8] 
for elemento in lista:    
  if(elemento % 2 == 0):        #si el resto entre dos es cero
    print(f'{elemento} es par')    
  else:        
    print(f'{elemento} es impar')
    break #si ejecutamos esto solo se va a ejecutar una vez porque una vez encontrado el impar rompe el bucle

#Ejemplo 3
lista = [1,2,3,4,5,6,7,8] 
for elemento in lista:    
  if(elemento % 2 == 0):
    print(f'{elemento} es par')    
  else:        
    pass #continua con la ejecución y si ejecuta la linea de abajo
    print(f'{elemento} es impar')
#Ejemplo4
lista = [1,2,3,4,5,6,7,8] 
for elemento in lista:    
  if(elemento % 2 == 0):
    print(f'{elemento} es par')    
  else:        
    continue #no continua con la linea de abajo, se la salta, pasa al siguiente valor 
    print(f'{elemento} es impar')
#Ejemplo5
lista = [1,2,3,4,5,6,7,8] 
for elemento in lista:    
  if(elemento % 2 == 0):
    break
    print(f'{elemento} es par')    
  else:        
    continue
    print(f'{elemento} es impar')
#solo se ejecuta dos veces, la primera no sale que el 1 es impar porque con el continue hace que pase a la siguiente condición, la segunda como resto igual a cero coge el break y se sale del bucle

 #Ejemplo6
lista = [1,2,3,4,5,6,7,8] 
for elemento in lista:    
  if(elemento % 2 == 0):
    continue
    print(f'{elemento} es par')    
  else:        
    continue
    print(f'{elemento} es impar')
#no se va a imprimir nada porque no va a llegar al print por el continue, pero se ejecuta las 8 veces porque se van cumpliendo las condiciones

'''
WHILE
Repetir una serie de sentencias según algún criterio.
La principal diferencia es que los bucles FOR tienen, por definición, ya establecido el límite de ciclos que va a realizar.
En cambio, en los bucles WHILE, el número de iteraciones (ciclos) puede cambiar dependiendo de dos factores:
-El valor del elemento con el que condiciona el bucle. Esto hace que puede que no se lleguen nunca a ejecutar o incluso se puedan dar casos de bucles infinitos.
-De las operaciones que se realicen dentro del bucle
'''
lista = [1,2,3,4,5,6,7,8] 
#Bucle WHILE para encontrar eliminar elementos hasta que la longitud sea 3
while (len(lista) > 3):    
  lista.pop() #pop va eliminando el ultimo elemento de la lista 
  print(lista)
'''
¡OJO! Uno de los mayores riesgos a los que se enfrenta un desarrollador cuando hace uso de bucles while, es al bucle infinito. Se trata de un fallo muy temido porque hace que el programa nunca llegue a terminar.
'''
# ¡Bucle INFINITO! Mucho cuidado
suma: int = 0
while True:
  suma+=1    
  print(suma)

'''
DO WHILE
Su principal diferencia con un bucle WHILE normal es que DO WHILE se ejecutaría siempre al menos una vez, mientras que un bucle WHILE, como hemos comentado antes, podría no llegar a ejecutarse nunca.
'''
#Python NO CUENTA con bucles DO WHILE, pero se pueden simular:
i = 1

while True: 
  print(i)      
  i = i + 1      
  if(i > 5): 
    break

'''
EJERCICIO
- Por consola el usuario debe acertar un número secreto
- Tiene 3 intentos
- Si acierta en el primer intento: Se suman 5 puntos y el resultado se multiplican por 2
- Si acierta en el segundo intento: Se suman 5 puntos
- Si acierta a la tercera: Se suma 2 puntos
- Si falla todas las veces: Se resta 2 puntos

'''
numeroElegido = int(input("Elige un número: "))
numeroBuscado = 300
intentos = 3

'''
while(numeroElegido % 2 != 0):
  numeroElegido = int(input("Vuelve a elegir un número: "))
'''

while(numeroElegido != numeroBuscado):
  if(numeroElegido > numeroBuscado):
    numeroElegido = int(input("Has fallado, el número buscado es más pequeño: "))
  else:
    numeroElegido = int(input("Has fallado, el número buscado es más grande: "))

print(f"Has ganado, el número era {numeroBuscado}")

'''
FUNCIONES
son un conjunto de sentencias/instrucciones aisladas/encapsuladas que permiten la reutilización de código de una tarea específica y recurrente. 
La ventajas principales de usar funciones son:
> Ahorran trabajo
> Simplifican el código
> Reducen el número de líneas
> Hacen que el código sea mantenible y extensible.
'''
def nombreFunción (parámetros) -> tipo_retorno:
  # declaración de variables	
  # y ejecución de código 
  

#Función básica en Python
miFuncion():  
  print(f"Esto es una función básica") 
# Llamamdo y ejecutando la función
miFuncion()

#Función con parámetros no tipados

def miFuncionConParametros(a: str,b: str):    
  print(f"¡{a}, {b}!") 
# llamando la función y pasándole algunos parámetros
miFuncionConParametros('Hola', 'Mundo')
miFuncionConParametros(a='Hola',b='Mundo')
miFuncionConParametros(b='Hola',a='Mundo')
miFuncionConParametros('Hola',b='Mundo')
miFuncionConParametros('Hola',a='Mundo')


#Función con muchos parámetros
def miFuncionConMultiplesParametros(*elementos) :    
  for elemento in elementos:        
    print(f"Elemento: {elemento}") 

# llamando la función y pasándole una lista de parámetros
lista: [int] = [1, 2, 3, 4, 5]
miFuncionConMultiplesParametros(lista)

miFuncionConMultiplesParametros(1,2,3,4,5)
miFuncionConMultiplesParametros([1,2,3,4,5])

'''
Paso de parámetros

-Por valor: pasamos únicamente el valor al parámetro y éste hará de nueva variable local dentro de la función. Es decir, si el valor del parámetro se modifica, el valor de la variable original no lo hace.

-Por referencia: En este caso, no se pasa el valor, sino la referencia (el punto de memoria donde el valor está guardado).
Por esto mismo, si dentro de la función el valor se modifica, también se modifica el valor de la variable original, ya que ambas estarían apuntando al mismo punto de la memoria.
'''
#Por referencia
#Los valores simples se pasan, por defecto, por valor
#Los valores complejos se pasan, por defecto, por referencia 

# las listas al ser complejos se pasan por referencia
# Esto quiere decir que si la función edita el parámetro, éste se edita también en origen 
def doblar_valores(numeros): 
  for i,n in enumerate(numeros):        
    numeros[i] *= 2

#Ahora hacemos uso de esta función y vemos como el valor original se modifica
# definiendo una variable que se va a pasar por referencia
  ns = [10,50,100]
  doblar_valores(ns)print(f"Lista Original Modificada: {ns}") 
  #[20, 100, 200]

# Para aquellos tipos de datos simples, si queremos el mismo comportamientode paso por referencia podemos: 
  
# SOBRESCRIBIR EL VALOR ORIGINAL CON EL VALOR DE RETURN DE LA FUNCIÓN
def doblar_valor(numero):   
  return numero * 2
  
n = 10
n = doblar_valor(n)
print(f"Valor original Modificado: {n}")


'''
FUNCIONES LAMBDA
Hacen uso del paradigma de programación funcional en el que podemos crear funciones rápidas y de consumo veloz sin necesidad de declarar una función clásica.
'''
lambda parámetros: expresión

al_cuadrado = lambda a: a**2
#llamando a la función lambda
print(al_cuadrado(2)) #imprimirá un 4



''' PASO POR REFERENCIA
Paso de parámetros por Referencia
-Los valores simples se pasan, por defecto, por valor
-Los valores complejos se pasan, por defecto, por referencia ''' 

# las listas al ser complejos se pasan por referencia
# Esto quiere decir que si la función edita el parámetro,
# éste se edita también en origen 
def doblar_valores(numeros):    
  for indice,numero in enumerate(numeros):        
    numeros[indice] *= 2
  
# definiendo una variable que se va a pasar por referencia
ns = [10,50,100]
doblar_valores(ns)

print(f"Lista Original Modificada: {ns}") 
# [20, 100, 200]

# SI NO QUEREMOS PASAR UNA LISTA COMO REFERENCIA, DEBEMOS REALIZAR UNA COPIA "AL VUELO"
# Ahora esta no se pasará por referencia, ya que haremos una copia del valor
ns = [10,50,100]
doblar_valores(ns[:])  
# Una copia al vuelo de una lista se realiza con [:]
# Esto hace que la lista original no se vea modificada
print(f"Lista Original No Modificada: {ns}") 
#[10, 50, 100]

# Para aquellos tipos de datos simples, si queremos el mismo comportamiento# de paso por referencia podemos: 
# SOBRESCRIBIR EL VALOR ORIGINAL CON EL VALOR DE RETURN DE LA FUNCIÓN
def doblar_valor(numero):    
  return numero * 2 
  
n = 10
doblar_valor(n)
n = doblar_valor(n)
print(f"Valor original Modificado: {n}")

''' FUNCIONES LAMBDA: 
Las funciones Lambda de Python son bastante habituales. 
'''
al_cuadrado = lambda a: a**2 

# llamando a la función lambda
print(al_cuadrado(2)) # imprimirá un 4



'''DEBUGGING
El debugging o también llamado proceso de depuración es la técnica que utilizan los desarrolladores para encontrar los errores de su código en tiempo de ejecución
'''


#EJERCICIO
#Por consola solicitar al usuario un número. El programa debe pedir números hasta que el usuario introduzca un año bisiesto.

anio = int(input("Escribe un año para comprobar si es bisiesto: "))

  #lógica
while anio %4 != 0:
  if anio % 4 != 0:
    print("El año no es bisiesto")
    anio = int(input("Escribe un año para comprobar si es bisiesto: "))
  elif anio % 100 == 0 and anio % 400 != 0:
    print("El año no es bisiesto")

print("Has acertado, enhorabuena")