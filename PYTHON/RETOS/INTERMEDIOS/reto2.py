articulo = input('Introduce el artículo que desea comprar: ')
precio = input('Introduzca precio del articulo: ')

carrito:bool = input("¿Introducir otro elemento al carrito?: ")

while carrito == True:
  ListaCompra = dict()
  ListaCompra = {
    'Artículo' : articulo,
    'Precio' : precio
  }
  if carrito == False:
    precio_total = sum(precio)
    print(*ListaCompra)
    print('El coste total de su compra es: ', {precio_total})