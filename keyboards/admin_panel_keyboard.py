from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_admin_panel():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    markup.add(
        KeyboardButton("📋 View All Feedbacks"),
        KeyboardButton("📤 Announcements"),
        KeyboardButton("🔙 Back to Main Menu")
        )
    

    return markup