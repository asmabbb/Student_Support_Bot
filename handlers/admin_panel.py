from bot_instance import bot
from config import ADMIN_ID
from database.models import get_all_feedbacks
from keyboards import main_keyboard, announcements_keyboard





# View All Feedbacks (Admins)
@bot.message_handler(func=lambda message: message.text == "📋 View All Feedbacks")
def view_all_feedback(message):

    feedbacks = get_all_feedbacks()

    if not feedbacks:
        bot.send_message(message.chat.id, "No feedbacks available.")
        return
    
    text = ""
    for fb in feedbacks:
            formatted_date = fb[3].strftime("%Y-%m-%d at %I:%M %p")
            text += f"👤 {fb[1]}    ({fb[0]})\n\n📝 {fb[2]}\n\n📅 {formatted_date}\n\n----------------------------------------------------------\n"

    bot.send_message(message.chat.id, text)







# Announcements Button
@bot.message_handler(func=lambda messages: messages.text == "📤 Announcements")
def announements(message):
     chat_id = message.chat.id
     bot.send_message(chat_id, "Announcements Section.", reply_markup=announcements_keyboard.announcements_keyboard())










# Back Button
@bot.message_handler(func=lambda message: message.text == "🔙 Back to Main Menu")
def back_to_main(message):
    is_admin = message.from_user.id in ADMIN_ID
    bot.send_message(message.chat.id, "Welcom back the main menu!", reply_markup=main_keyboard.main_menu(is_admin))
