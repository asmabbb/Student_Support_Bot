from bot_instance import bot
from config import ADMIN_ID
from database.models import get_all_users
from keyboards.announcements_keyboard import announcements_keyboard, announcement_confirmation
from keyboards.admin_panel_keyboard import get_admin_panel


# A temporary storage for the announcement
announcement_mode_admins = {}

# Handle making an announcement

@bot.message_handler(func=lambda message: message.text == "📢 Make an Announcement")
def make_announcement(message):
    chat_id = message.chat.id

    if message.from_user.id not in ADMIN_ID:
        return

    bot.send_message(chat_id, "Send the announcement: ")
    bot.register_next_step_handler(message, preview_announcement)





def preview_announcement(message):
    user_id = message.from_user.id
    chat_id = message.chat.id



    if message.from_user.id not in ADMIN_ID:
        return
    
    announcement_text = message.text

    #Store announcement temporarily
    announcement_mode_admins[user_id] = announcement_text

    bot.send_message(chat_id, f"📢 Announcement Preview:\n\n{announcement_text}", reply_markup=announcement_confirmation())




# Handle announcement confirmation

@bot.callback_query_handler(func=lambda call: call.data in ["confirm_announcement", "cancel_announcement"])
def handle_announcement_confirmation(call):
    admin_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    option = call.data

    if admin_id not in ADMIN_ID:
        return
    
    if option == "cancel_announcement":
        announcement_mode_admins.pop(admin_id, None)
        bot.edit_message_text("❌ Announcement cancelled.", chat_id, message_id)
        return
    
    if option == "confirm_announcement":
        announcement_text = announcement_mode_admins.get(admin_id)

        if not announcement_text:
            bot.answer_callback_query(call.id, "No annoncement found.", show_alert=True)
            return
        
        users = get_all_users()

        sent_count = 0

        for user in users:
            try:
                bot.send_message(user[0], f"📢 Announcement:\n\n{announcement_text}")
                sent_count += 1
            except:
                pass # Incase a user blocked bot or error

        announcement_mode_admins.pop(admin_id, None)

        bot.edit_message_text(f"✅ Announcement sent to {sent_count} users.", chat_id, message_id)






# Back to Admin Panel button
@bot.message_handler(func=lambda message: message.text == "🔙 Back to Admin Panel")
def back_to_admin_panel(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Admin Panel.", reply_markup=get_admin_panel())