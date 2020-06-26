# import logging, time
# import os
# import random
# import sys
# import requests
# from telegram.ext import *
# from telegram import *
# from funciones import *


# # Enabling logging
# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logger = logging.getLogger()

# # Getting mode, so we could define run function for local and Heroku setup
# mode = os.getenv("MODE")
# # mode = 'dev'
# TOKEN = os.getenv("TOKEN")
# if mode == "dev":
#     def run(updater):
#         updater.start_polling()
# else :
#     def run(updater):
#         PORT = int(os.environ.get("PORT", "8443"))
#         HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
#         # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
#         updater.start_webhook(listen="0.0.0.0",
#                               port=PORT,
#                               url_path=TOKEN)
#         updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))


# # FUNCIONES DEL BOT

# def start(bot, update):
#   """ This function will be executed when '/start' command is received """

#   message = "Bienvenido al asistente personal! \n\n/list para ver tus opciones"
#   bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
#   bot.send_message(chat_id=update.message.chat_id, text=message)
 

# def random_number (bot, update):
#     # Creating a handler-function for /random command
#     update.message.reply_text(funcion_random_number())

# def noticias (bot, update, args):
    
   
#     if len(args) == 0 :
#       medio = 'none'
#     else :
#       medio = args[0]
#     for entrada in funcion_noticias(medio):
#       update.message.reply_text(entrada)
#       # bot.send_message(chat_id=update.message.chat_id,
#                      # parse_mode='markdown', text=entrada)

# def track_mensajeria(bot, update, args):
#   logger.info(args)
#   message = funcion_track_mensajeria(args)
#   bot.send_message(chat_id=update.message.chat_id, text=message)


# def perrete (bot, update):
#   bot.send_photo(chat_id=update.message.chat_id, photo=funcion_get_perrete())

# def plain_text(bot, update):
#     """ This function will be executed when plain text message is received """
#     bot.send_message(chat_id=update.message.chat_id,
#                      parse_mode='markdown', text=funcion_contar_palabras(update.message.text))


# def listar (bot, update):
#     """ This function will be executed when plain text message is received """
#     text = update.message.text
#     opciones = ''
#     for func in arrayFunciones:
#       opciones += '/'+func+'\n'
#     message = "*Comandos*\n*########*\n"+opciones
#     bot.send_message(chat_id=update.message.chat_id,
#                      parse_mode='markdown', text=message)



# if __name__ == '__main__':
#     logger.info("Starting bot")
#     updater = Updater(TOKEN)

#     arrayFunciones = ['start','list','mensajeria','perrete','random','noticias']


#     # Command handlers
#     start_handler = CommandHandler('start', start)
#     list_handler = CommandHandler('list', listar)
#     mensajeria_handler = CommandHandler('mensajeria', track_mensajeria, pass_args=True)
#     perrete_handler = CommandHandler('perrete', perrete)
#     random_handler = CommandHandler("random", random_number)
#     noticias_handler = CommandHandler("noticias", noticias, pass_args=True)

#     # Other handlers
#     plain_text_handler = MessageHandler(Filters.text, plain_text)



#     # Add the handlers to the bot
    
#     updater.dispatcher.add_handler(start_handler)
#     updater.dispatcher.add_handler(mensajeria_handler)
#     updater.dispatcher.add_handler(list_handler)
#     updater.dispatcher.add_handler(perrete_handler)
#     updater.dispatcher.add_handler(plain_text_handler)
#     updater.dispatcher.add_handler(random_handler)
#     updater.dispatcher.add_handler(noticias_handler)



# run(updater)



#!/usr/bin/python3
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
############################### Bot ############################################
def start(bot, update):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

# and so on for every callback_data option
def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Option 1', callback_data='m1')],
              [InlineKeyboardButton('Option 2', callback_data='m2')],
              [InlineKeyboardButton('Option 3', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

def first_menu_message():
  return 'Choose the submenu in first menu:'

def second_menu_message():
  return 'Choose the submenu in second menu:'

############################# Handlers #########################################
updater = Updater('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu,
                                                    pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu,
                                                    pattern='m2_1'))

updater.start_polling()
################################################################################