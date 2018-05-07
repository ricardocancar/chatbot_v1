#!/usr/bin/python
##librerias
import logging
from DAO import *
from pymongo import MongoClient
from texto import *
from bson.son import SON
import re

## variable global
client = MongoClient("localhost",27017)
db = client.datos_valencia


def sumaImpuesto(impuesto):
    suma = []
    if impuesto == "impuestos" or impuesto == "impost":
        suma = [
            "$impuestos.IVTNU Personas Físicas",
            "$impuestos.IVTNU Personas Jurídicas",
            "$impuestos.IAE",
            "$impuestos.IVTM Personas Físicas",
            "$impuestos.IVTM Personas Jurídicas",
            "$impuestos.IBI Personas Físicas",
            "$impuestos.IBI Personas Jurídicas"
            ]

    elif impuesto=="IVTNU":
        suma = [
            "$impuestos.IVTNU Personas Físicas",
            "$impuestos.IVTNU Personas Jurídicas"
            ]

    elif impuesto=="IAE":
        suma = [
            "$impuestos.IAE"
            ]

    elif impuesto=="IVTM":
        suma = [
            "$impuestos.IVTM Personas Físicas",
            "$impuestos.IVTM Personas Jurídicas"
            ]

    elif impuesto=="IBI":
        suma = [
            "$impuestos.IBI Personas Físicas",
            "$impuestos.IBI Personas Jurídicas"
            ]

    return suma


def impuestos_barrio(barrio,impuesto,anio,key,leng):
  ##this function return the sum of taxes pay in each neighbor  
  regx = re.compile("^{}".format(barrio), re.IGNORECASE)
  dbBarrios = db.barrio_impuesto
  if anio == '':
    anio = 2016
  if len(list(dbBarrios.find({"anio":int(anio)}))) > 0: ### check if we have data for that year
    pipeline = [
        {"$match": {"sinonimos": regx, "anio": anio}},
        {"$sort": SON([("anio", -1)])},          ##SON function is use to maintain the sort in python dictionary
        {"$limit": 1},
        {"$project": {
            "_id": "$barrio",
            "valor": {"$sum": []},
            "anyo": "$anio"
            }
         }
        ]

    try:
      suma = sumaImpuesto(impuesto)
    except Exception as e:
      logging.exception("- Error en suma: ")
  

    try:
      pipeline[3]["$project"]["valor"]["$sum"].extend(suma)
    except Exception as e:
      logging.exception("- Error al añadir suma a pipeline: ")
  
    try:
      respuesta = list(dbBarrios.aggregate(pipeline))
    except Exception as e:
      logging.exception("- Error conexión PagoBarrios: ")
  
    return respuesta_bot(key,leng).format(barrio,respuesta[0]['valor'],impuesto,anio)
  else:
    return respuesta_bot('resErrorano',leng).format(anio)

if __name__ =='__main__':
   print(impuestos_barrio('La Bega Baixa','IBI',2016,'res.Impuesto','Cast'))
