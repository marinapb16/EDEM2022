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

listaDiscos = [ {'Nombre' : 'dmer', 'Artista' : 'Bad Bunny', 'Año' : 2019, 'precio' : 20.4, 'Género' : 'Reggeaton'},
                {'Nombre' : 'Canto del loco', 'Artista' : 'Pepa', 'Año' : 2017, 'precio' : 34.6, 'Género' : 'Pop'},
                {'Nombre' : 'LALA', 'Artista' : 'Pepe', 'Año' : 2026, 'precio' : 32.6, 'Género' : 'Black Metal'}]

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