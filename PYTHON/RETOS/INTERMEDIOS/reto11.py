#RETO 11
#Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
#NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
#El programa debe mostrar las siguientes opciones para que escoja el usuario:
#(1) Añadir un cliente
#(2) Eliminar cliente por NIF
#(3) Mostrar Cliente por NIF
#(4) Listar TODOS os clientes
#(5) Mostrar ÚNICAMENTE los clientes preferentes
#(6) Finalizar Programa

class Clientes:
  #atributos de clase
  NIF:str
  Nombre:str
  Apellidos:str
  Telefono:str
  email:str
  preferente:bool

  # Método constructor
  def __init__(self, NIF, Nombre, Apellidos, Telefono, email, preferente):
    self.NIF = NIF
    self.Nombre = Nombre
    self.Apellidos = Apellidos
    self.Telefono = Telefono
    self.email = email
    self.preferente = preferente