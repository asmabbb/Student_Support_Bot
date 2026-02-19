from bot_instance import bot
from keyboards import main_keyboard
from config import ADMIN_ID


# Start Handler
@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    is_admin = message.from_user.id in ADMIN_ID
    bot.send_message(chat_id, f"Hello {message.from_user.first_name}!\nWelcom to CETSU Student Support Bot.", reply_markup=main_keyboard.main_menu(is_admin))
