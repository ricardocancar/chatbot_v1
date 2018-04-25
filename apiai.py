#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests
import json

#from variables import *


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    apiAccess = 'b895aef28b814f6fb3c795a264d09b5c'
    apiDeveloperAccess = '4106b2509662420c802f62322319a1a9'

except Exception as e:
    print(time.strftime("%c"), "- Error al cargar tokens de api.ai: ", type(e), e)

#baseURL = "https://api.api.ai/v1/"
baseURL = "https://api.dialogflow.com/v1/"
#baseURL = "https://api.dialogflow.com/v1/query?v=20150910&query=hola&lang=es&sessionId=500737046&timezone=Europe/Madrid"
#v = 20170605 # fecha en formato AAAAMMDD
#v = 20170712 intent
v = 20150910 #one click integration
APIAI_LANG = "es"

headers = {
    'Authorization': 'Bearer '+ apiAccess,
    "Content-Type":"application/json; charset=utf-8"
    }


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sendQuery(texto, chat_id, idioma, nombreUsuario):
    contexto = [{
        "name": "usuario",
        "parameters": { "idioma": idioma, "nombre": nombreUsuario },
        "lifespan": 1
        }]
    payload = {
        "query": texto,
        "v": v,
        "sessionId": chat_id,
        "contexts": contexto,
        "lang": APIAI_LANG
        }

    url = baseURL+"query"

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    return r

if __name__=='__main__':
  res = sendQuery('cuanto ganas',"500737046", 'espanol','ricardo')
  print(res)
  if res.status_code == 200:
    
    res = res.json()
    print(res)	#['result']['resolvedQuery'])
  #print(sendQuery('prueba 1', '1234', 'español','ricardo'))









#130da067-d0fa-45ff-97b4-c8105d1255aa








