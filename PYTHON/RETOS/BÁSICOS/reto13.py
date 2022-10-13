#RETO 13
#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base 
# como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

#función para calcular el area de un triangulo
def areatriangulo (base,altura):
  area = (base*altura)/2
  return area
  
base = float(input('Introduce la base del triángulo: '))
altura = float(input('Introduce la altura del triángulo: '))

result = areatriangulo(base,altura)

print("El area de un triángulo de", base, 'por', altura, 'es', result)

#función para calcular area de un circulo
from math import pi
def areacirculo (radio):
  area_circulo = pi*(radio**2)
  return area_circulo
  
radio = float(input('Introduce el radio del circulo: '))

result = areacirculo(radio)

print("El area de un circulo de radio", radio, "es", result)
