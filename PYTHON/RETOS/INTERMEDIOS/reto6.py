#RETO 6
#Escribe un programa que pida al usuario una palabra por consola y devuelva si se trata de un palíndormo
#Palíndromo: Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda

palabra = str(input("Introduce una palabra: "))

inversa = palabra[::-1]

if palabra == inversa:
    print("La palabra que ha introducido es un palíndromo")
else:
    print("La palabra introducida no es un palíndromo")