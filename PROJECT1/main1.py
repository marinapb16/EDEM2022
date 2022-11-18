import requests
import time
import json
import csv

while True:
  url = 'https://geoportal.valencia.es/apps/OpenData/Trafico/tra_espiras_p.json'
  r = requests.get(url)
  response = r.json()
  datos: str = response
  #completo = datos[0]
  '''rase = completo['quote']
  personaje = completo['character']
  cita = frase + " " + personaje'''
  print(response)
  
  '''cita = {"quote": frase, "character": personaje}
  if personaje == "Lisa Simpson":'''
  with open('Trafico.csv', 'a+') as f:
      wr = csv.DictWriter(f, response.keys())
      wr.writerow(response)
      
  '''elif personaje == "Homer Simpson":
    with open('Homer/Homer.csv', 'a+') as f:
     wr = csv.DictWriter(f, cita.keys())
     wr.writerow(cita)

  else:
    direccion = personaje +'.csv'
    direccion = direccion.replace(' ','_')
      
    with open(direccion, 'w+') as f:
     wr = csv.DictWriter(f, cita.keys())
     wr.writerow(cita)'''


  
[
 {
   "quote": "Shoplifting is a victimless crime, like punching someone in the dark.",
   "character": "Nelson Muntz",
   "image" : "https://cdn.glitch.com/3c3ffadc-3406-4440-bb95-d40ec8fcde72%2FNelsonMuntz.png?1497567511185",
   "characterDirection" : "Left"
 }
]
          
     
  
      
    

#time.sleep(5)