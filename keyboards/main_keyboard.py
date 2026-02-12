from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# Main menu (Reply Keyboard)
main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=1)
main_menu.add(
    KeyboardButton("CETSU Bots"),
    KeyboardButton("Feedback")
)


# Bot menu (Inline Keyboard)
roadMap = InlineKeyboardButton("RoadMap", url="https://t.me/RoadMap_CETSU_bot")
comp_lost = InlineKeyboardButton("Complaints/ Lost & founds", url="https://t.me/TicketCETSu_bot")
syllabus = InlineKeyboardButton("Syllabus", url="https://t.me/CETCu_bot")

bots_menu = InlineKeyboardMarkup(row_width=1)
bots_menu.add(roadMap, comp_lost, syllabus)