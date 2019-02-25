from telegram.ext import *
import db


updater = Updater(token="727202433:AAGXUfFgx9qDML4t2jibu5dRQcIMqlilXFk")
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, напиши мне 'баланс' что бы узнать баланс")


def textMessage(bot, update):
    response = update.message.text.lower()

    if response == "баланс":
        b = db.GetUserStats(update.message.chat_id)
        try:
            bot.send_message(chat_id=update.message.chat_id, text=f"Твой баланс: {b['money']}")
        except TypeError:
            print("Error")


start_command_handler = CommandHandler("start", startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)
updater.idle()
