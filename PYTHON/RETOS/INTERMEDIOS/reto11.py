#RETO 11
#Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes 
# en un diccionario u objeto literal en el que disponga de:
#NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
#El programa debe mostrar las siguientes opciones para que escoja el usuario:
#(1) Añadir un cliente
#(2) Eliminar cliente por NIF
#(3) Mostrar Cliente por NIF
#(4) Listar TODOS os clientes
#(5) Mostrar ÚNICAMENTE los clientes preferentes
#(6) Finalizar Programa

#creo lista vacía de clientes
clientes = []
#Definimos las distintas opciones que el cliente puede realizar
def opciones ():
  print('''Hola! ¿Qué desea hacer?:
          (1) Añadir un cliente
          (2) Eliminar cliente por NIF
          (3) Mostrar cliente por NIF
          (4) Listar todos los clientes
          (5) Mostrar únicamente los clientes preferentes
          (6) FInalizar programa''')
  seleccion = int(input('Seleccione la operación que quiere realizar: '))
  while seleccion:
    if seleccion == 1:
      addcliente()
    elif seleccion == 2:
      eliminarcliente()
    elif seleccion == 3:
      muestracliente()
    elif seleccion == 4:
      listaclientes()
    elif seleccion == 5:
      preferentes()
    elif seleccion == 6:
      print('Hasta la próxima!')
      exit()
    else:
      seleccion = int(input('Su selección ha de ser un número del 1 al 6'))

#Añadir cliente
def addcliente():
 
  NIF = str(input('Introduce el NIF: \n'))
  nombre = str(input('Introduce el nombre: \n'))
  telefono = str(input('Introduce el telefono: \n'))
  email = str(input('Intorduce el email: \n'))
  preferente = input('El cliente cliente es preferente (si/no)')

  if preferente == 'si':
    preferente = True
  elif preferente == 'no':
    preferente = False

  cliente = {"NIF" : NIF,
            "Nombre" : nombre,
            "Telefono" : telefono,
            "Email" : email,
            "Preferente" : preferente}

  clientes.append(cliente)
  opciones()

#Eliminar cliente por NIF
def eliminarcliente():
  nif = input('Introduzca el NIF del cliente que quiere eliminar: ')
  for i in clientes:
    if i["NIF"]==nif:
      clientes.remove(i)
      print("El cliente ha sido eliminado")
    else:
      print('El NIF introducido no pertenece a ningún cliente y no se puede eliminar')
  opciones()

#Mostrar cliente por NIF
def muestracliente():
  nif = input('Introduzca el NIF del cliente que quiere visualizar: ')
  for i in clientes:
    if i["NIF"]== nif:
      print(f'NIF: {i["NIF"]}, Nombre: {i["Nombre"]}, Telefono: {i["Telefono"]}, Email: {i["Email"]}, Preferente: {i["Preferente"]}' )
    else:
      print('El NIF introducido no pertenece a ningún cliente y no se puede eliminar')
  opciones()
  
#Listar todos los clientes
def listaclientes():
  for idx, i in enumerate(clientes):
    print(f'NIF: {i["NIF"]}, Nombre: {i["Nombre"]}, Telefono: {i["Telefono"]}, Email: {i["Email"]}, Preferente: {i["Preferente"]}' )
  opciones()

#Mostrar los clientes preferentes
def preferentes():
  for i in clientes:
    if i["Preferente"] == True:
      print(f'NIF: {i["NIF"]}, Nombre: {i["Nombre"]}, Telefono: {i["Telefono"]}, Email: {i["Email"]}, Preferente: {i["Preferente"]}' )
    else:
      print("No hay clientes preferentes")
  opciones()

opciones()