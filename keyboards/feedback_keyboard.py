from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def feedback_menu_keyboard(is_admin = False):
    feedback_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    feedback_menu.add(KeyboardButton("✍️ Make Feedback"))
    feedback_menu.add(KeyboardButton("📂 View My Feedback"))

    if is_admin:
        feedback_menu.add(KeyboardButton("📊 View All Feedbacks"))

    feedback_menu.add(KeyboardButton("⬅️ Back"))

    return feedback_menu