from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup



# ---- Announcements Keyboard ----
def announcements_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    markup.add(
        KeyboardButton("📢 Make an Announcement"),
        KeyboardButton("🔙 Back to Admin Panel")
    )




# ---- Confirmation Keyboard ----

def announcement_confirmation():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.add(
        InlineKeyboardButton("✅ Confirm", callback_data="confirm_announcement"),
        InlineKeyboardButton("❌ Cancel", callback_data="cancel_announcement")
    )

    return markup