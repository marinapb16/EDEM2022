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



listaDiscos = [ {'Nombre' : 'YHLT', 'Artista' : 'Bad Bunny', 'Año' : 2019, 'precio' : 20.4, 'Género' : 'Reggeaton'},
                {'Nombre' : 'Canto del loco', 'Artista' : 'Pepa', 'Año' : 2017, 'precio' : 34.6, 'Género' : 'Pop'},
                {'Nombre' : 'LALA', 'Artista' : 'Pepe', 'Año' : 2026, 'precio' : 32.6, 'Género' : 'Black Metal'}]

#print(listaDiscos) Check1

#Bucle para imprimir por consola los discos de la lista para el usuario
for idx, disco in enumerate(listaDiscos):
    print(f'Número disco {idx+1}: Nombre {disco["Nombre"]}, Artista {disco["Artista"]}, Precio {disco["precio"]}, Estilo {disco["Género"]}') #+1 porque el 0 lo queremos para mostrar ticket de compra

#input para que el usuario seleccione un disco
seleccion = int(input("Selecciona un disco de la lista (0 para terminar la compra) "))-1
#check2

if listaDiscos[seleccion]['Género'] == 'Electro' or listaDiscos[seleccion]['Género'] == 'Black Metal':
    precioCarrito = listaDiscos[seleccion]['precio'] * 0.7
else:
    precioCarrito = listaDiscos[seleccion]['precio']


print(precioCarrito)

