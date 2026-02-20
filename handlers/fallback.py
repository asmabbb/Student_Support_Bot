from bot_instance import bot
from keyboards import main_keyboard
from config import ADMIN_ID

@bot.message_handler(func=lambda message: True)
def fallback(message):
    chat_id = message.chat.id
    is_admin = message.from_user.id in ADMIN_ID
    bot.send_message(chat_id, "🤖: لم أفهم ماذا تقصد!\nمن فضلك إختر خياراً من القائمة.", reply_markup=main_keyboard.main_menu(is_admin))