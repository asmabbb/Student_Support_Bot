from bot_instance import bot
from keyboards import main_keyboard
from config import ADMIN_ID
from database.models import save_user


# Start Handler
@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    is_admin = message.from_user.id in ADMIN_ID

    user_id = message.from_user.id
    username = message.from_user.username

    save_user(user_id, username)

    bot.send_message(chat_id, f" {message.from_user.first_name}👋 أهلا بك!\n مرحبًا بك في بوت دعم اتحاد طلبة كلية التقنية الإلكترونية.\n ", reply_markup=main_keyboard.main_menu(is_admin))
