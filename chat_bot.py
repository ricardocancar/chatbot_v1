#!/usr/bin/python
# -*- coding: utf-8 -*-
import texto
import ayuntament
import logging 
from variables import *
from DAO import*
from telegram import  (ReplyKeyboardMarkup, ReplyKeyboardRemove, User, Bot,InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, ConversationHandler, Filters,RegexHandler,CallbackQueryHandler)
#filename="chat_bot.log"
logging.basicConfig(filename="chat_bot.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


tecladoIdioma = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Valencià', callback_data='Val'),
     InlineKeyboardButton(text='Castellano', callback_data='Cast')],#Dentro de la lista para que se vea en la misma línea
  ])
  


def start(bot,update):
  ### le pasamos la id de telegram para registrar usuario nuevo. 
  if not existe_Usuario(update.message.chat_id):
    insertarNuevoUsuario(update.message.chat_id)
  else:
    actualizarUsuario(update.message.chat_id)
  leng = get_idioma(update.message.chat_id)

  bot.sendMessage(chat_id = update.message.chat_id, text= texto.greetings('comandoStart',leng))
  update.message.reply_text('Idioma:', reply_markup=tecladoIdioma)
  
def idioma(bot,update):
  leng = get_idioma(update.message.chat_id)

  bot.sendMessage(chat_id = update.message.chat_id, text= texto.greetings('comandoIdioma',leng))
  update.message.reply_text('Idioma:', reply_markup=tecladoIdioma)

def button(bot,update):
    query = update.callback_query

    resultado = True
    if resultado == True:
        actualizarIdioma(query.message.chat.id,query.data)
        bot.answerCallbackQuery(callback_query_id= query.id, text=texto.greetings('pulsarBotonIdioma',query.data))
        bot.sendMessage(chat_id =query.message.chat_id, text=texto.greetings('respuestaCambioIdioma',query.data))
    else:
        bot.sendMessage(chat_id= query.message.chat_id, text=texto.greetings('respuestaCambioIdiomaError',query.data))

def mensaje(bot,update):
   if not existe_Usuario(update.message.chat_id):
      insertarNuevoUsuario(update.message.chat_id)
   else:
      actualizarUsuario(update.message.chat_id)

   bot.sendMessage(chat_id=update.message.chat_id, text='aqui va la respuesta del bot')
   insertarMensaje(update.message)

def main():
<<<<<<< HEAD
  updater = Updater(Token)
=======
  updater = Updater('')
>>>>>>> origin/master
  
  updater.start_polling()
  updater.dispatcher.add_handler(CommandHandler('start',start))
  updater.dispatcher.add_handler(CommandHandler('inicio',start))
  updater.dispatcher.add_handler(CommandHandler('idioma',idioma))
  updater.dispatcher.add_handler(MessageHandler(Filters.text,mensaje))
  updater.dispatcher.add_handler(CallbackQueryHandler(button))
  #updater.start_webhook(listen='0.0.0.0',
  #                    port=8443,
  #                    url_path=variables.Token_bot,
  #                    key='private.key',
  #                    cert='cert.pem',
  #                    webhook_url='{}:8443/{}'.format(variables.url, variables.Token_bot))

  updater.idle()

if __name__ == '__main__':
  main()
