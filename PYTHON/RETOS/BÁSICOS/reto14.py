#RETO 14
#Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro,
#  obteniendo por parámetro la longitud del mismo.

#from reto13 import areacirculo
#from reto13 import radio

#si se tiene el ejercicio 13 abierto nos vale con importar la función ya definida
#por si acaso la vuelvo a poner en este ejercicio para que funcione sin necesidad del 14

from math import pi
def areacirculo (radio):
  area_circulo = pi*(radio**2)
  return area_circulo
  
radio = float(input('Introduce el radio del circulo: '))

def volumencilindro (longitud):
  r = areacirculo(radio)
  return r*longitud

longitud = float(input('Introduce la longitud del cilindro: '))

result = volumencilindro(longitud)

print("El volumen del cilindro de radio", radio, "y longitud", longitud, "es", result)