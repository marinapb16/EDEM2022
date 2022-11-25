##PRODUCTO (nombre de la clase en mayúscula pero los atributos en minúscula)
#Qué va a tener el producto
# -id
# -nombre
# -precio
# -categoría
# -coste
# -color

## Ikea es nuestra tienda de muebles 

#Armario
# -puertas
# -altura
# -anchura

##Silla
# -patas
# -material

from enum import Enum
#creamos una categoría de enumeración para luego poder darle a nuestro producto la numeración perteneciente
# según su categoría y para limitar las categorias que queremos que sean

class Categoria(Enum):
    COCINA = 1
    SALON = 2
    TERRAZA = 3

class Color(Enum):
    BLANCO = 1
    NEGRO = 2
    MARRON = 3

class Producto():
    nombre: str
    precio: float
    categoria: Categoria
    coste : float
    color : Color

    def __init__(self, nombre:str, precio:float, categoria:Categoria, coste:float, color:Color):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.coste = coste
        self.color = color







