import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


import telebot
from config import API_TOKEN
from keyboards import main_keyboard


# Making the bot object
bot = telebot.TeleBot(token=API_TOKEN)


# Start Handler
@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Hello {message.from_user.first_name}!\nWelcom to CET Student Support Bot.", reply_markup=main_keyboard.main_menu)

bot.polling()