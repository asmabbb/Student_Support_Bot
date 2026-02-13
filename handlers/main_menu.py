from bot_instance import bot
from keyboards import main_keyboard


# Start Handler
@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Hello {message.from_user.first_name}!\nWelcom to CETSU Student Support Bot.", reply_markup=main_keyboard.main_menu)
