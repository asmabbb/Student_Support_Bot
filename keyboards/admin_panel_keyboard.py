from telebot.types import ReplyKeyboardMarkup

def get_admin_panel():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("📋 View All Feedback")
    markup.add("🔙 Back to Main Menu")

    return markup