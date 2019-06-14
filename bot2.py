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





def start(bot, update):
  """ This function will be executed when '/start' command is received """

  message = "Bienvenido al asistente personal! \n\n/list para ver tus opciones"
  bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
  time.sleep(2)
  bot.send_message(chat_id=update.message.chat_id, text=message)
 

def random_number (bot, update):
    # Creating a handler-function for /random command
    update.message.reply_text(funcion_random_number())



def track_mensajeria(bot, update, args):
  logger.info(args)
  message = funcion_track_mensajeria(args)
  bot.send_message(chat_id=update.message.chat_id, text=message)


def perrete (bot, update):
  bot.send_photo(chat_id=update.message.chat_id, photo=funcion_get_perrete())



def plain_text(bot, update):
    """ This function will be executed when plain text message is received """
    bot.send_message(chat_id=update.message.chat_id,
                     parse_mode='markdown', text=funcion_contar_palabras(update.message.text))


def listar (bot, update):
    """ This function will be executed when plain text message is received """
    text = update.message.text
    opciones = ''
    for func in arrayFunciones:
      opciones += '/'+func+'\n'
    message = "*Comandos*\n*########*\n"+opciones
    bot.send_message(chat_id=update.message.chat_id,
                     parse_mode='markdown', text=message)



if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(TOKEN)

    arrayFunciones = ['start','list','mensajeria','perrete','random']


    # Command handlers
    start_handler = CommandHandler('start', start)
    list_handler = CommandHandler('list', listar)
    mensajeria_handler = CommandHandler('mensajeria', track_mensajeria, pass_args=True)
    perrete_handler = CommandHandler('perrete', perrete)
    random_handler = CommandHandler("random", random_number)

    # Other handlers
    plain_text_handler = MessageHandler(Filters.text, plain_text)



    # Add the handlers to the bot
    
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(mensajeria_handler)
    updater.dispatcher.add_handler(list_handler)
    updater.dispatcher.add_handler(perrete_handler)
    updater.dispatcher.add_handler(plain_text_handler)
    updater.dispatcher.add_handler(random_handler)



run(updater)
