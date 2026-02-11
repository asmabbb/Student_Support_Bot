from telebot.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=1)
main_menu.add(
    KeyboardButton("syllabus bot"),
    KeyboardButton("complaints bot"),
    KeyboardButton("lost & founds bot"),
    KeyboardButton("choose your profession bot"),
    KeyboardButton("feedback")
)
