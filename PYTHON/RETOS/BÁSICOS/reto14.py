#RETO 14
#Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro,
#  obteniendo por parámetro la longitud del mismo.
from reto13 import areacirculo
from reto13 import radio

def volumencirculo (longitud):
  r = areacirculo(radio)
  return r*longitud

longitud = float(input('Introduce la longitud del cilindro: '))

result = volumencirculo(longitud)

print("El volumen del cilindro de longitud", longitud, "es", result)