#RETO 11
#Escribe un programa que pida al usuario los siguientes datos por consola:
#-Título de la película
#-Director
#-Año
#-País
#E introduzca esos valores en una variable GLOBAL llamada "pelicula"´


titulo_pelicula = input('Introduce el Título de una película: ')

director = input('Introduce el nombre del director de la película: ')

anio = int(input('Introduce el año de la película: '))

pais = input('País en el que se grabó la película: ')

pelicula = dict()

pelicula = {
  'Título de la película' : titulo_pelicula,
  'Director película' : director,
  'Año película' : anio,
  'País' : pais
}
