print("A continuación le vamos a realizar una serie de preguntas para ayudarle a encontrar la mejor zona para vivir:")

sanitarios = int(input('Valore del 1 al 10 cuanto le importa tener centros sanitarios cerca: '))

if sanitarios==1 or sanitarios==2:
    print("Ciutat Vella, Benimaclet o Pobles de l'Oest")
elif sanitarios==3 or sanitarios==4:
    print("Eixample o Jesús")
elif sanitarios ==5 or sanitarios==6:
    print("Extramurs, La Saïdia, El Pla del Real, L'Olivereta, Patraix, Camins al Grau, Algirós, Rascanya o Benicalap ")
elif sanitarios==6 or sanitarios==7:
    print("Pobles del Nord")
elif sanitarios==8:
    print("Campanar")
elif sanitarios==9 or sanitarios ==10:
    print("Quatre Carrers o Poblats Marítims")
else:
    sanitarios = int(input('Su selección ha de ser un número del 1 al 10'))

colegios = int(input("Valore del 1 al 10 cuanto le importa tener centros educativos por su zona: "))