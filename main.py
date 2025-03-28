import telebot
from db.actions import *

bot = telebot.TeleBot("7605881665:AAFpJWhgENPjn-C4t8PkJhTHY-eH3UV1e3g")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    messageId = message.chat.id
    # ////////////////////////////////////////
    if not checkIfItIsMe(message.from_user.id):
        bot.send_message(messageId, "This bot is private")
        return
    # ////////////////////////////////////////
    bot.send_message(messageId, selectAllFromHistory())
    bot.send_message(messageId, selectAllFromParams())

def checkIfItIsMe(id):
    return id == 893695047

bot.infinity_polling()