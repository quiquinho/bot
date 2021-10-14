#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""Simple inline keyboard bot with multiple CallbackQueryHandlers.
This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined as callback query handler. Then, those functions are
passed to the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot that uses inline keyboard that has multiple CallbackQueryHandlers arranged in a
ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line to stop the bot.
"""
import logging,os
from funciones import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
# Stages
FIRST, SECOND = range(2)
# Callback data
ONE, TWO, FARO, AS, PAIS, MARCA = range(6)


# PRIMER NIVEL
def one(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Faro de vigo", callback_data=str(FARO)),
            InlineKeyboardButton("El Pais", callback_data=str(PAIS)),
        ],[
            
            InlineKeyboardButton("Diario As", callback_data=str(AS)),
            InlineKeyboardButton("Marca", callback_data=str(MARCA)),
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Estas en la sección de noticias, selecciona un medio", reply_markup=reply_markup
    )
    return FIRST
def two(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Volver", callback_data=str(ONE)),
            InlineKeyboardButton("Medio", callback_data=str(FARO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Selecciona opción en meteo", reply_markup=reply_markup
    )
    return FIRST

# SEGUNDO NIVEL
def faro(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    news = funcion_noticias('faro').reverse()
    for new in news:
        escribir(query , context, new )
    
    keyboard = [
        [
            InlineKeyboardButton("Si, volver a empezar", callback_data=str(ONE)),
            InlineKeyboardButton("Nah, Ya basta ...", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text="Deseas volver a empezar?"
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=reply_markup)
    # Transfer to conversation state `SECOND`
    return SECOND
def diarioAs(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    news = funcion_noticias('as').reverse()
    for new in news:
        escribir(query , context, new )
    
    keyboard = [
        [
            InlineKeyboardButton("Si, volver a empezar", callback_data=str(ONE)),
            InlineKeyboardButton("Nah, Ya basta ...", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text="Deseas volver a empezar?"
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=reply_markup)
    # Transfer to conversation state `SECOND`
    return SECOND
def pais(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    news = funcion_noticias('el_pais').reverse()
    news = news[:10]
    for new in news:
        escribir(query , context, new )
    keyboard = [
        [
            InlineKeyboardButton("Si, volver a empezar", callback_data=str(ONE)),
            InlineKeyboardButton("Nah, Ya basta ...", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text="Deseas volver a empezar?"
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=reply_markup)
    # Transfer to conversation state `SECOND`
    return SECOND
def marca(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()


    news = funcion_noticias('marca').reverse()
    for new in news:
        escribir(query , context, new )
    
    keyboard = [
        [
            InlineKeyboardButton("Si, volver a empezar", callback_data=str(ONE)),
            InlineKeyboardButton("Nah, Ya basta ...", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text="Deseas volver a empezar?"
    context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=reply_markup)
    # Transfer to conversation state `SECOND`
    return SECOND

#AUXILIARES
def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("Noticias", callback_data=str(ONE)),
            InlineKeyboardButton("Meteo", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Bienvenido al asistente de Quique, selecciona una opción", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST
def start_over(update: Update, context: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Noticias", callback_data=str(ONE)),
            InlineKeyboardButton("Meteo", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="Bienvenido al asistente de Quique, selecciona una opción", reply_markup=reply_markup)
    return FIRST
def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Nos vemos en la proxima!")
    escribir(query , context, '/start' )
    return ConversationHandler.END
def escribir(query , context, texto ):
    context.bot.send_message(chat_id=query.message.chat.id, text=texto)
def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv("TOKEN"), use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(faro, pattern='^' + str(FARO) + '$'),
                CallbackQueryHandler(diarioAs, pattern='^' + str(AS) + '$'),
                CallbackQueryHandler(pais, pattern='^' + str(PAIS) + '$'),
                CallbackQueryHandler(marca, pattern='^' + str(MARCA) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

