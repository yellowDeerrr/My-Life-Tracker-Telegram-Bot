import telebot
from actions import *

bot = telebot.TeleBot("7627299223:AAEecfLK-l1JrofjSAeUoU36RZ7-rZVXenc")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    messageId = message.chat.id
    # ////////////////////////////////////////
    if not checkIfItIsMe(message.from_user.id):
        bot.send_message(messageId, "This bot is private")
        return
    # ////////////////////////////////////////
    bot.send_message(messageId, 'test')
    bot.send_message(messageId, selectAllFromHistory())
    bot.send_message(messageId, selectAllFromParams())

def checkIfItIsMe(id):
    return id == 893695047

def main():
    bot.infinity_polling()
if __name__ == "__main__":
    main()