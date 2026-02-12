from bot_instance import bot
from keyboards import main_keyboard

from database.models import save_feedback


feedback_mode_users = set()

# creating the menu option response handler:
@bot.message_handler(content_types=["text"], func=lambda message: message.text in ['CETSU Bots', 'Feedback'])
def option_handler(message):
    option = message.text
    chat_id = message.chat.id
    if option == "CETSU Bots":
        bot.send_message(chat_id, "These are the CET Student Union bots: ", reply_markup=main_keyboard.bots_menu)

    elif option == "Feedback":
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