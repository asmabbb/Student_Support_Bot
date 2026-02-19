from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_admin_panel():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton("📋 View All Feedbacks"))
    markup.add(KeyboardButton("🔙 Back to Main Menu"))

    return markup