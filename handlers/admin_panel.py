from bot_instance import bot
from config import ADMIN_ID
from database.models import get_all_feedbacks
from keyboards import main_keyboard





# View All Feedbacks (Admins)
@bot.message_handler(func=lambda message: message.text == "📋 View All Feedbacks")
def view_all_feedback(message):

    feedbacks = get_all_feedbacks()

    if not feedbacks:
        bot.send_message(message.chat.id, "No feedbacks available.")
        return
    
    text = ""
    for fb in feedbacks:
            text += f"👤 {fb[1]} ({fb[0]})\n\n📝 {fb[2]}\n\n📅 {fb[3]}\n\n\n--------------------"

    bot.send_message(message.chat.id, text)





# Back Button
@bot.message_handler(func=lambda message: message.text == "🔙 Back to Main Menu")
def back_to_main(message):
    is_admin = message.from_user.id in ADMIN_ID
    bot.send_message(message.chat.id, "Welcom back the main menu!", reply_markup=main_keyboard.main_menu(is_admin))
