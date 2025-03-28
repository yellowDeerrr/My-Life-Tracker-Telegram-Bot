import telebot

bot = telebot.TeleBot("7605881665:AAFpJWhgENPjn-C4t8PkJhTHY-eH3UV1e3g")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # ////////////////////////////////////////
    if not checkIfItIsMe(message.from_user.id):
        bot.send_message(message.chat.id, "This bot is private")
        return
    # ////////////////////////////////////////
    bot.send_message(message.chat.id, message.from_user.id)

def checkIfItIsMe(id):
    return id == 893695047

bot.infinity_polling()