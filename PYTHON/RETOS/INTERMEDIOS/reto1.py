#Una tienda vende Discos de música (unos muñecos muy graciosos). 
# Con la idea de vender un stock almacenado durante meses, se decide que discos de género "Black Metal" 
# y "Electro" tienen un descuento del 30%.
#Cada disco (usa un diccionario para esto) tendrá:
#Nombre
#Artista
#Año
#Precio
#Género (solo pueden ser de los siguientes)
#Pop
#Electro
#Reggaeton
#Rock
#Metal
#Death Metal
#Black Metal
#Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario 
# pueda elegir el disco a comprar.
#Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra 
# (puedes coger la fecha actual a través de datetime), el dinero que se ahorra el usuario 
# y el coste final de la compra.

from datetime import datetime

listaDiscos = [ {'Nombre' : 'Born this way', 'Artista' : 'Lady Gaga', 'Año' : 2011, 'precio' : 20.4, 'Género' : 'Pop'},
                {'Nombre' : 'Private dancer', 'Artista' : 'Tina turner', 'Año' : 1984, 'precio' : 34.6, 'Género' : 'Pop'},
                {'Nombre' : 'Ross from friends', 'Artista' : 'Tread', 'Año' : 2018, 'precio' : 22.6, 'Género' : 'Electro'},
                {'Nombre' : 'Azure', 'Artista' : 'SkyH1', 'Año' : 2021, 'precio' : 31.7, 'Género' : 'Electro'},
                {'Nombre' : 'The last don', 'Artista' : 'Don Omar', 'Año' : 2003, 'precio' : 10.3, 'Género' : 'Reggaeton'},
                {'Nombre' : 'Un verano sin ti', 'Artista' : 'Bad Bunny', 'Año' : 2022, 'precio' : 27.5, 'Género' : 'Reggaeton'},
                {'Nombre' : 'The Dark side of the moon', 'Artista' : 'Pink Floyd', 'Año' : 1973, 'precio' : 38.4, 'Género' : 'Rock'},
                {'Nombre' : 'Black in Black', 'Artista' : 'ACDC', 'Año' : 1980, 'precio' : 17.8, 'Género' : 'Rock'},
                {'Nombre' : 'Torn Arteries', 'Artista' : 'Carcass', 'Año' : 2021, 'precio' : 18.9, 'Género' : 'Metal'},
                {'Nombre' : 'Senjutsu', 'Artista' : 'Iron Maiden', 'Año' : 2021, 'precio' : 32.6, 'Género' : 'Metal'},
                {'Nombre' : 'Focus', 'Artista' : 'Cynic', 'Año' : 1993, 'precio' : 28.4, 'Género' : 'Death Metal'},
                {'Nombre' : 'Human', 'Artista' : 'Death', 'Año' : 2021, 'precio' : 27.1, 'Género' : 'Death Metal'},
                {'Nombre' : 'Black Metal', 'Artista' : 'Venom', 'Año' : 1982, 'precio' : 38.4, 'Género' : 'Black Metal'},
                {'Nombre' : 'Filosofem', 'Artista' : 'Burzum', 'Año' : 1996, 'precio' : 23.8, 'Género' : 'Black Metal'} ]

#print(listaDiscos) Check1


#Bucle para imprimir por consola los discos de la lista para el usuario
for idx, disco in enumerate(listaDiscos):
    print(f'Número disco {idx+1}: Nombre {disco["Nombre"]}, Artista {disco["Artista"]}, Precio {disco["precio"]}, Estilo {disco["Género"]}') #+1 porque el 0 lo queremos para mostrar ticket de compra

carrito = list()
while True:

    #input para que el usuario seleccione un disco
    seleccion = int(input("Selecciona un disco de la lista (0 para terminar la compra) "))-1
    #check2

    if seleccion == -1:
        break   #para no caer en un bucle infinito, si pulsa 0, salimos del bucle
    else:
        carrito.append({'Nombre':listaDiscos[seleccion]["Nombre"], 'precio':listaDiscos[seleccion]["precio"], 'Género':listaDiscos[seleccion]["Género"]})

#print(carrito)
#para comprobar que el append está funcionando bien

precioCarrito = 0
cantidadDescuento = 0

#FORMA 1
#for i in carrito: 
#    if i['Género] == 'Electro' or i['Género'] == 'Black Metal'
# ...
#Esto sería otra manera de hacer el for, en i tenemos guardado un diccionario

#FORMA 2
for i in range(len(carrito)): #en este caso i es un número porque recorre longitud del diccionario

    if carrito[i]['Género'] == 'Electro' or carrito[i]['Género'] == 'Black Metal':
        precioCarrito += carrito[i]['precio'] * 0.7
        cantidadDescuento += carrito[i]['precio'] * 0.3
    else:
        precioCarrito += carrito[i]['precio']

#FORMA 3
# for idx,i in enumerate(carrito):

#      if i['Género] == 'Electro' or i['Género] == 'Black Metal':
# ...
#Utilizando el indice
#       if carrito[idx]['Género'] == 'Electro' or carrito[idx]['Género'] == 'Black Metal'
#...

print(datetime.now())
print('El precio total de su compra es: ', precioCarrito, '€')
print('Su ahorro en esta compra ha sido de ', cantidadDescuento, '€')