from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# Main menu (Reply Keyboard)
def main_menu(is_admin=False):
    main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=1)
    main_menu.add(
        KeyboardButton("🤖 CETSU Bots"),
        KeyboardButton("📢 Announcements & Group Chats"),
        KeyboardButton("📥 Feedback")
    )
    if is_admin:
        main_menu.add(KeyboardButton("⚙️ Admin Panel"))

    return main_menu


# Bot menu (Inline Keyboard)
roadMap = InlineKeyboardButton("🗺️ أرسم مسارك", url="https://t.me/RoadMap_CETSU_bot")
comp_lost = InlineKeyboardButton("📝 المفقودات/الشكاوي", url="https://t.me/TicketCETSu_bot")
syllabus = InlineKeyboardButton("📚 المناهج", url="https://t.me/CETCu_bot")

bots_menu = InlineKeyboardMarkup(row_width=1)
bots_menu.add(roadMap, comp_lost, syllabus)


# Join Us Menu:
announce = InlineKeyboardButton("الإعلانات", url="https://t.me/Ta3alm_ET")
group_chat = InlineKeyboardButton("مجموعة الطلبة", url="https://t.me/etstudents_e")

join_us_menu = InlineKeyboardMarkup(row_width=2)
join_us_menu.add(announce, group_chat)