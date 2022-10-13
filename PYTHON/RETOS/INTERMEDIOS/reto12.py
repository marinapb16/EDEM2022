#RETO 12
#Escribe un script de código que haga al usuario introducir 8 alturas de edificios (deben ser float) 
# y que saque por consola las 3 más altas (haz uso de sorted).

altura1 = float(input('Introduce altura edificio: '))
altura2 = float(input('Introduce altura edificio: '))
altura3 = float(input('Introduce altura edificio: '))
altura4 = float(input('Introduce altura edificio: '))
altura5 = float(input('Introduce altura edificio: '))
altura6 = float(input('Introduce altura edificio: '))
altura7 = float(input('Introduce altura edificio: '))
altura8 = float(input('Introduce altura edificio: '))

ListaAlturas = [altura1, altura2, altura3, altura4, altura5, altura6, altura7, altura8]

sorted_ListaAlturas = sorted(ListaAlturas)

print('Las tres alturas más altas de las introducidas son: ', sorted_ListaAlturas[5], sorted_ListaAlturas[6], "y", sorted_ListaAlturas[7])