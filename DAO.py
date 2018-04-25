#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pymongo
import logging
from datetime import datetime # Para insertar la fecha actual
import time #Librería con funcionalidades manipular y dar formato a fechas y horas


#from variables import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    urlMongoDB = 'localhost' #URL_de_MongoDB
    port = 27017
except Exception as e:
    print (time.strftime("%c"), "- Error al cargar la URL del MongoDB: ", type(e), e)

# urlMongoDB = "mongodb://valenciaApp:valenciaApp@ds127321.mlab.com:27321/datos_valencia"

client = pymongo.MongoClient(urlMongoDB,port)
db = client.prueba  #db = client.get_default_database() # Accedemos a la BD donde tenemos las colecciones
dbUsuarios = db.usuarios
dbMensajes = db.mensajes

#msg['from']={'nombre': 'Arnau', '_id': 192224003, 'idioma': 'cast'}


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def insertarNuevoUsuario(idUsario):
    query = {
        '_id': idUsario,
        'idioma': "Cast",
        'fechaInsercion': datetime.now(),
        'fechaUltimoAcceso': datetime.now(),
        'numPreguntas': 1
    }

    try:
        dbUsuarios.insert_one(query)
    except Exception as e:
        print(time.strftime("%c"), "- Error al insertar Usuario: ", type(e), e)

def existe_Usuario(idUsuario):
  #### de vueleve true si el usuario exite
  query = {
        '_id': idUsuario
  }
  usuario = dbUsuarios.find_one(query)
  if usuario == 'None':
    return False
  else:
    return True
      

def get_idioma(idUsuario):
  query = {
        '_id': idUsuario
  } 
  usuario = dbUsuarios.find_one(query)
  idioma = usuario['idioma']
  return idioma
  
    
  
def buscarUsuario(idUsario):
    query = {
        '_id': idUsario
    }
    try:
        cursor = dbUsuarios.find_one(query)
    except Exception as e:
        print(time.strftime("%c"), "- Error en buscar Usuario: ", type(e), e)

    return cursor

def insertarMensaje(mensaje):
    
    #fechaUnix = mensaje['date'].now()
    #mensaje['date'] = fechaUnix #datetime.fromtimestamp(fechaUnix)
    mensaje = {
       'date': mensaje.date.now().strftime("%Y-%m-%d %H:%M:%S"),
       'idUsuario': mensaje.chat.id,
       'texto': mensaje.text,
       'lenguaje':mensaje.from_user.language_code}
    try:
        
        dbMensajes.insert_one(mensaje)
    except Exception as e:
        print(time.strftime("%c"), "- Error en insertar mensaje: ", type(e), e)
        logging.exception( "- Error en insertar mensaje: ")

def actualizarUsuario(idUsario):
    query = {
        '_id': idUsario
    }
    update = { '$inc': { 'numPreguntas': 1}, '$set': {'fechaUltimoAcceso': datetime.now()}}

    try:
        dbUsuarios.update_one(query,update)
        return True
    except Exception as e:
        print(time.strftime("%c"), "- Error en actualizar Usuario: ", type(e), e)


def actualizarIdioma(idUsario,idioma):
    query = {
        '_id': idUsario
    }
    update = {'$set': {'idioma': idioma}}
    try:
        result = dbUsuarios.update_one(query,update)
        return True
    except Exception as e:
        print(time.strftime("%c"), "- Error en actualizar idioma: ", type(e), e)

def actualizarRespuesta(message_id, chat_id, respuesta, accion):
    query = {
        'chat.id': chat_id,
        'message_id': message_id
    }
    update = {'$set': {'respuesta_accion': accion, 'respuesta_texto':respuesta}}
    try:
        dbMensajes.update_one(query,update)
    except Exception as e:
        print(time.strftime("%c"), "- Error en actualizar respuesta: ", type(e), e)
