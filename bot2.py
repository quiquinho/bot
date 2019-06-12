import logging
import os
import random
import sys
import requests
from telegram.ext import *


# Enabling logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Getting mode, so we could define run function for local and Heroku setup
mode = os.getenv("MODE")
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
  message = "Bienvenido al asistente personal!"
  bot.send_message(chat_id=update.message.chat_id, text=message)
  message = "*Comandos*\n*########*\n/start\n/hello\n/list\n/foto"
  bot.send_message(chat_id=update.message.chat_id,
                     parse_mode='markdown', text=message)

def random (bot, update):
    # Creating a handler-function for /random command
    number = random.randint(0, 10)
    logger.info("User {} randomed number {}".format(update.effective_user["id"], number))
    update.message.reply_text("Random number: {}".format(number))

def hello(bot, update):
  """ This function will be executed when '/hello' command is received """
  greeting = "Hi there, {}".format(update.effective_user.username)
  bot.send_message(chat_id=update.message.chat_id, text=greeting)


def add(bot, update, args):
  """ This function will be executed when '/add arg1, arg2, ...' command is received """

  # First converts the string list to a int list and then add all the elems
  result = sum(map(int, args))
  message = "The result is: {}".format(result)
  bot.send_message(chat_id=update.message.chat_id, text=message)


def get_url():
  contents = requests.get('https://random.dog/woof.json').json()
  url = contents['url'] 
  return url

def foto (bot, update):
  
  url = get_url()
  bot.send_photo(chat_id=update.message.chat_id, photo=url)



def plain_text(bot, update):
    """ This function will be executed when plain text message is received """
    text = update.message.text
    words_count = len(text.split())
    letters_count = len(''.join(text).replace(' ', ''))
    message = "Your message has {words} words and {letters} letters".format(
        words=words_count, letters=letters_count)
    bot.send_message(chat_id=update.message.chat_id,
                     parse_mode='markdown', text=message)


def list (bot, update):
    """ This function will be executed when plain text message is received """
    text = update.message.text
    message = "*Comandos*\n*########*\n"
    bot.send_message(chat_id=update.message.chat_id,
                     parse_mode='markdown', text=message)







if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(TOKEN)




    # Command handlers
    start_handler = CommandHandler('start', start)
    hello_handler = CommandHandler('hello', hello)
    list_handler = CommandHandler('list', list)
    add_handler = CommandHandler('add', add, pass_args=True)
    foto_handler = CommandHandler('foto', foto)
    random_handler = CommandHandler("random", random)

    # Other handlers
    plain_text_handler = MessageHandler(Filters.text, plain_text)



    # Add the handlers to the bot
    
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(hello_handler)
    updater.dispatcher.add_handler(add_handler)
    updater.dispatcher.add_handler(list_handler)
    updater.dispatcher.add_handler(foto_handler)
    updater.dispatcher.add_handler(plain_text_handler)
    updater.dispatcher.add_handler(random_handler)



    run(updater)
