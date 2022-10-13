#RETO 14
# Partiendo de las siguientes cadenas de texto:
miCodigo = 'print("Hola Mundo")'
otroCodigo = """
def multiplicar(x,y):
    return x*y

print('Multiplica: 2 * 4: ',multiplicar(2,4))
"""
#Haz uso de exec() para ejecutar ambas operaciones

miCodigo = 'print("Hola Mundo")'
otroCodigo = """
def multiplicar(x,y):
    return x*y

print('Multiplica: 2 * 4: ',multiplicar(2,4))
"""

exec(miCodigo) #¿como ejecuto ambas operaciones?