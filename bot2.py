import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton


INPUT_TEXT = 0


def start(update, context):

    update.message.reply_text(
        text='Hola, bienvenido, qué deseas hacer?\n\nUsa /qr para generar un código qr.',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='News', callback_data='noticias')],
            [InlineKeyboardButton(text='Meteo', callback_data='meteo')],
        ])
    )


def noticias_command_handler(update, context):
    update.message.reply_text('Envíame el medio')
    return INPUT_TEXT

def meteo_command_handler(update, context):
    update.message.reply_text('Envíame el dia')
    return INPUT_TEXT



def noticias_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Envíame el medio'
    )
    return INPUT_TEXT

def meteo_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Envíame el dia'
    )
    return INPUT_TEXT








def obtener_noticias(update, context):
    text = update.message.text
    chat = update.message.chat
    context.bot.send_message(chat_id=update.message.chat_id, text=text)
    # context.bot.send_message(chat_id=update.message.chat_id, text='/start')
    return 'noticias'
    return ConversationHandler.END


def obtener_meteo(update, context):
    print('meteo')
    text = update.message.text
    chat = update.message.chat
    print(chat)
    return ConversationHandler.END




def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv("TOKEN"), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(
        entry_points=[

            CommandHandler('noticias', noticias_command_handler),
            CallbackQueryHandler(pattern='noticias', callback=noticias_callback_handler),
            CommandHandler('meteo', meteo_command_handler),
            CallbackQueryHandler(pattern='meteo', callback=meteo_callback_handler),            
        ],

        states={
            INPUT_TEXT: [MessageHandler(Filters.text, obtener_noticias)]
        },

        fallbacks=[],
        conversation_timeout=6
    ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':

    main()