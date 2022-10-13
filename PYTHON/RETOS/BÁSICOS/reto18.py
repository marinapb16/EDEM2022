#RETO 18
#Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. 
# La función debe tener la siguiente firma:

def eliminar(text: str,n: int) -> str:   return text[:n]+text[n+1:]

print(eliminar('Madrid', 0)) #adrid
print(eliminar('Madrid', 3)) #Madid
print(eliminar('Madrid', 5)) #Madri