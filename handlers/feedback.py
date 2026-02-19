from bot_instance import bot
from config import ADMIN_ID
from keyboards import main_keyboard
from keyboards import feedback_keyboard
from keyboards import admin_panel_keyboard
from database.models import save_feedback, get_all_feedbacks, get_user_feedbacks

from database.models import save_feedback


feedback_mode_users = set()

# creating the menu option response handler:
@bot.message_handler(content_types=["text"], func=lambda message: message.text in ['🤖 CETSU Bots', '📢 Announcements & Group Chats', '📥 Feedback'])
def option_handler(message):
    option = message.text
    chat_id = message.chat.id

    if option == "🤖 CETSU Bots":
        bot.send_message(chat_id, "These are the CET Student Union bots: ", reply_markup=main_keyboard.bots_menu)

    elif option == "📥 Feedback":
        
        bot.send_message(chat_id, "Feedback Section", reply_markup=feedback_keyboard.feedback_menu_keyboard())

    elif option == "📢 Announcements & Group Chats":
        bot.send_message(chat_id, "Know the latest announcemnts from here: ", reply_markup=main_keyboard.join_us_menu)

    elif option == "⚙️ Admin Panel":
        bot.send_message(chat_id, "Admin Panel:", reply_markup=admin_panel_keyboard.get_admin_panel())
        


# Make feedback 
@bot.message_handler(func=lambda message: message.text == "✍️ Submit Feedback")
def make_feedback(message):
    chat_id = message.chat.id
    feedback_mode_users.add(chat_id)
    bot.send_message(chat_id, f"Ok {message.from_user.first_name}, you are now in feedback mode.\nSend your feedback or type /cancel.")
    bot.register_next_step_handler(message, process_feedback)




def process_feedback(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.from_user.username
    text = message.text
    
    if chat_id not in feedback_mode_users:
        return
    
    if message.text == "/cancel":
        feedback_mode_users.remove(chat_id)
        bot.send_message(chat_id, "Feedback mode cancelled.")
        return
    
    if text.startswith("/") or text == "Feedback":
        bot.send_message(chat_id, "⚠️ You are in feedback mode!\nSend your feedback or type /cancel.")
        bot.register_next_step_handler(message, process_feedback)
        return
    
    save_feedback(user_id, username, text)
    
    bot.reply_to(message, "✅ Your message has been saved and will be reviewed. \nThank you for your input.")
    feedback_mode_users.remove(chat_id)


# View My Feedback
@bot.message_handler(func=lambda message: message.text == "📂 View My Feedback")
def view_my_feedback(message):
    
    feedbacks = get_user_feedbacks(message.from_user.id)

    if not feedbacks:
        bot.send_message(message.chat.id, "You haven't submitted any feedbacks yet.")
        return
    
    text = ""
    for fb in feedbacks:
        text += f"📝 {fb[0]}\n📅 {fb[1]}\n\n"

    bot.send_message(message.chat.id, text)


# # View All Feedbacks (Admins)
# @bot.message_handler(func=lambda message: message.text == "📊 View All Feedbacks")
# def view_all_feedback(message):

#     if message.from_user.id not in ADMIN_ID:
#         bot.send_message(message.chat.id, "Unauthorized.")
#         return
    
#     feedbacks = get_all_feedbacks()

#     if not feedbacks:
#         bot.send_message(message.chat.id, "No feedbacks available.")
#         return
    
#     text = ""
#     for fb in feedbacks:
#             text += f"👤 {fb[1]} ({fb[0]})\n📝 {fb[2]}\n📅 {fb[3]}\n\n"

#     bot.send_message(message.chat.id, text)



# Back Button
@bot.message_handler(func=lambda message: message.text == "🔙 Back to Main Menu")
def back_to_main(message):
    bot.send_message(message.chat.id, "Welcom back the main menu!", reply_markup=main_keyboard.main_menu)


# Fallback Function
@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(
        message.chat.id,
        "🤖 I didn't understand that. \nPlease choose an option from the menu.",
        reply_markup=main_keyboard.main_menu
    )
