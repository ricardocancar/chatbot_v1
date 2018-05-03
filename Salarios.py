#!/usr/bin/python
from pymongo import MongoClient
from texto import *
import re
import logging



client = MongoClient("localhost",27017)
db = client.datos_valencia

def salarios(nombre,key,idioma):
  try:
     regx = re.compile("^{}".format(nombre), re.IGNORECASE)
     nomina=list(db.salarios.find({"nombre": regx}))
  except Exception as e:
     logging.exception("error al buscar el nombre del {} alto cargo".format(nombre))
     return respuesta_bot("errorNoResult",idioma)
  if len(nomina) == 0:
    return respuesta_bot("errorNoResult",idioma)
  if len(nomina) == 1:
    return respuestas_bot(key,idioma)[0].format(nombre,int(nomina[0]['salario']),nomina[0]['cargo'])
  if len(nomina) > 1:
    return respuesta_bot("errorManyResult",idioma)

def cargos(cargo,key,idioma):
  try:
    nomina=db.salarios.find({"cargo":cargo})
    return respuestas_bot(key,idioma)[1].format(cargo,int(nomina[0]['salario']))
    
  except Exception as e:
      logging.exception("error al buscar {} en nuestra base de datos".format(cargo)) 
      return respuesta_bot("errorNoResult",idioma)

if __name__=='__main__':
  print(salarios("María","res.Salario","Cast"))


