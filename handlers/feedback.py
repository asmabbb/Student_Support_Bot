from bot_instance import bot
from keyboards import main_keyboard

# creating the menu option response handler:
@bot.message_handler(content_types=["text"], func=lambda message: message.text in ['CETSU Bots', 'Feedback'])
def option_handler(message):
    option = message.text
    chat_id = message.chat.id
    if option == "CETSU Bots":
        bot.send_message(chat_id, "These are the CET Student Union bots: ", reply_markup=main_keyboard.bots_menu)

    elif option == "Feedback":
        bot.send_message(chat_id, f"Ok {message.from_user.first_name}, you are in feedback mode.\nSend your feedback or press /cancel")
        bot.register_next_step_handler(message, process_feedback)

def process_feedback(message):
    feedback = message.text
    bot.reply_to(message, f"You message:{feedback}\nWill be forwarded to the admins of the bot.\nThank you for your input.")