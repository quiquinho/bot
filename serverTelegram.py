from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import requests

def start(bot, update):
  """ This function will be executed when '/start' command is received """
  message = "Bienvenido al asistente personal!"
  bot.send_message(chat_id=update.message.chat_id, text=message)
  message = "*Comandos*\n*########*\n/start\n/hello\n/list\n/foto"
  bot.send_message(chat_id=update.message.chat_id,
                     parse_mode='markdown', text=message)


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

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

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
    message = "*Comandos*\n*########*\n/start\n/hello\n/list\n/foto"
    bot.send_message(chat_id=update.message.chat_id,
                     parse_mode='markdown', text=message)



def main(bot_token):
  """ Main function of the bot """
  updater = Updater(token=bot_token)
  dispatcher = updater.dispatcher

  # Command handlers
  start_handler = CommandHandler('start', start)
  hello_handler = CommandHandler('hello', hello)
  list_handler = CommandHandler('list', list)
  add_handler = CommandHandler('add', add, pass_args=True)
  foto_handler = CommandHandler('foto', foto)

  # Other handlers
  plain_text_handler = MessageHandler(Filters.text, plain_text)
  unknown_handler = MessageHandler(Filters.command, unknown)



  # Add the handlers to the bot
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(hello_handler)
  dispatcher.add_handler(add_handler)
  dispatcher.add_handler(list_handler)
  dispatcher.add_handler(foto_handler)
  dispatcher.add_handler(plain_text_handler)
  dispatcher.add_handler(unknown_handler)

  # Starting the bot
  updater.start_polling()


if __name__ == "__main__":
  TOKEN = "872232476:AAEHbPGevOpuSb3cEgl0AYxf5VGQPwam4kg"
  main(TOKEN)