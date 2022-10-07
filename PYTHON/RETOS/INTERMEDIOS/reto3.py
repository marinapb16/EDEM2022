personas = ["Edu", "Julio", "Marina"]

deuda = 0
for nombre in personas:
  print('Hola', nombre)
  edad = int(input('Introduzca su edad: '))
  ingresos = int(input('Introduzca sus ingresos mensuales: '))
  if edad < 16 :
    print('Usted no debe pagar impuestos!')

  else:
    if ingresos < 800:
      deuda = ingresos * (10/100)
    elif ingresos > 800 and ingresos < 2000:
      deuda = ingresos * (30/100)
    else:
      deuda = ingresos * (50/100)

  deuda_anual = deuda*12

  print('Su endeudamiento en este año va a ser igual a:',   {deuda_anual})
