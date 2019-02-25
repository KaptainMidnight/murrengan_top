from telegram.ext import *
import db
import random

updater = Updater(token="720140452:AAHJ2fQXSp9WZuz39OdV_eMrShwa7rLZcmc")
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Напиши 'помощь' что бы посмотреть все команды")


def textMessage(bot, update):
    response = update.message.text.lower()
    user_status = db.GetUserStats(update.message.chat_id)
    if response == "баланс":
        try:
            bot.send_message(chat_id=update.message.chat_id, text=f"Твой баланс: {user_status['money']}")
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Ты зарегистрирован, напиши еще раз баланс")
    elif response == "профиль":
        bot.send_message(chat_id=update.message.chat_id,
                         text=f"🖥Твой ID: {user_status['id']}\n💰Баланс: {user_status['money']}")
    elif response == "помощь":
        bot.send_message(chat_id=update.message.chat_id,
                         text="Профиль - для просмотра профиля\nБаланс - просмотр баланса\nКазино сумма - для игры в казино")
    elif response.split()[0] == "казино":
        if int(user_status['money']) < int(response.split()[1]):
            bot.send_message(chat_id=update.message.chat_id, text="У тебя не хватает денег!")
            return
        else:
            r = random.randint(0, 100)
            if r >= 50:
                db.addMoney(update.message.chat_id, int(response.split()[1]), 1)
                bot.send_message(chat_id=update.message.chat_id, text="Поздравляю, ты выйграл")
            else:
                db.addMoney(update.message.chat_id, int(response.split()[1]), 2)
                bot.send_message(chat_id=update.message.chat_id, text="Прости, но ты проиграл")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Я тебя не понял")


start_command_handler = CommandHandler("start", startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)
updater.idle()
