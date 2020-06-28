import logging, time
import os
import random
import sys
import requests
from telegram.ext import *
from telegram import *
from funciones import *



# Enabling logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Getting mode, so we could define run function for local and Heroku setup
mode = os.getenv("MODE")
# mode = 'dev'
TOKEN = os.getenv("TOKEN")
if mode == "dev":
    def run(updater):
        updater.start_polling()
else :
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))


# FUNCIONES DEL BOT

# def start(bot, update):
#   """ This function will be executed when '/start' command is received """

#   message = "Bienvenido al asistente personal! \n\n/list para ver tus opciones"
#   bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
#   bot.send_message(chat_id=update.message.chat_id, text=message)

def listar (bot, update):
    """ This function will be executed when plain text message is received """
    text = update.message.text
    opciones = ''
    for func in arrayFunciones:
      opciones += '/'+func+'\n'
    message = "*Comandos*\n*########*\n"+opciones
    bot.send_message(chat_id=update.message.chat_id,
                     parse_mode='markdown', text=message)

def start (bot, update):
    """ This function will be executed when plain text message is received """



    text = update.message.text
    keyboard = [
                  [
                    InlineKeyboardButton("🗼 Faro de Vigo", callback_data='Faro'),
                    InlineKeyboardButton("⚽ Marca", callback_data='marca'),
                    InlineKeyboardButton("🇪🇸 El Pais", callback_data='el_pais')
                  ],
                  [
                    InlineKeyboardButton("💻 Xataka", callback_data='xataka'),
                    InlineKeyboardButton("🐢 Microsiervos", callback_data='msv'),
                    InlineKeyboardButton("🇬🇧 BBC", callback_data='bbc')
                  ], 
                  [
                    InlineKeyboardButton("🗽 New York Times", callback_data='nyt'),
                    InlineKeyboardButton("📘 Cole", callback_data='cole'),
                    InlineKeyboardButton("👑 Coronavirus", callback_data='coronavirus')
                  ]
                ]
 
    reply_markup = InlineKeyboardMarkup(keyboard)
 
    update.message.reply_text('Selecciona tu medio:', reply_markup=reply_markup)    

def button(bot, update):
    query = update.callback_query
    
    print(query.data)
    for entrada in funcion_noticias(query.data):
      query.message.reply_text(entrada)
    bot.send_message(chat_id=query.message.chat_id,
                     parse_mode='markdown', text='/start')


if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(TOKEN)

    arrayFunciones = ['start','list','menu']

    # Command handlers
    start_handler = CommandHandler('start', start)
    list_handler = CommandHandler('list', listar)



    # Add the handlers to the bot
    
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(list_handler)

    updater.dispatcher.add_handler(CallbackQueryHandler(button))




run(updater)


