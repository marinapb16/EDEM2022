#RETO 8
#Escribe una función que reciba un número entero positivo y devuelva su factorial.

n = int(input('Introduce un número entero positivo: '))
fact = 1
  
for i in range(1,n+1):
    fact = fact * i
      
print ("El factorial de", n, "es ", end="")
print (fact)