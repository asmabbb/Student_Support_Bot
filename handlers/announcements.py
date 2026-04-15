from bot_instance import bot
from config import ADMIN_ID
from database.models import get_all_users
from keyboards.announcements_keyboard import announcement_confirmation
from keyboards.admin_panel_keyboard import get_admin_panel

import time 
import threading
from telebot.apihelper import ApiTelegramException


# A temporary storage for the announcement
announcement_mode_admins = {}

# Handle making an announcement

@bot.message_handler(func=lambda message: message.text in ["📢 Make an Announcement", "🔙 Back to Admin Panel"] )
def announcements_handler(message):
    chat_id = message.chat.id
    option = message.text

    if message.from_user.id not in ADMIN_ID:
        return
    
    if option == "📢 Make an Announcement":
    
        announcement_mode_admins[message.from_user.id] = True

        bot.send_message(chat_id, "Send the announcement: ")

    elif option == "🔙 Back to Admin Panel":
        bot.send_message(chat_id, "Admin Panel.", reply_markup=get_admin_panel())






@bot.message_handler(content_types=["text", "photo", "video"], func=lambda message: message.from_user.id in announcement_mode_admins)
def preview_announcement(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if user_id not in ADMIN_ID:
        return
    
    if user_id not in announcement_mode_admins:
        return
    

    # Save message info instead of just text
    announcement_mode_admins[message.from_user.id] = {
        "chat_id": message.chat.id, 
        "message_id":message.message_id
        }
    bot.send_message(chat_id, "⚠️ Announcement Preview — Confirm?", reply_markup=announcement_confirmation())




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
        data = announcement_mode_admins.get(admin_id)

        if not data:
            bot.answer_callback_query(call.id, "No annoncement found.")
            return
        
        else:
            # start broadcast in background thread
            thread = threading.Thread(
                target=broadcast_announcement,
                args=(data, chat_id, message_id)
            )

            thread.start()

            bot.edit_message_text(
                "📡 Sending announcement to all users...",
                chat_id,
                message_id
            )

            announcement_mode_admins.pop(admin_id, None)

            bot.edit_message_text(f"✅ Announcement sent to {sent_count} users.", chat_id, message_id)






# Broadcast Function
def broadcast_announcement(data, chat_id, message_id):
    users = get_all_users()

    sent_count = 0

    for user in users:
        try:
            bot.copy_message(
                chat_id=user[0],
                from_chat_id=data["chat_id"],
                message_id=data["message_id"]
             )
            
            sent_count += 1

            # Telegram safe speed (about 25 messages per second for 5000 users)
            time.sleep(0.04)

        except ApiTelegramException as e:
             
             # Telegram rate limit protection
             if "Too Many Requests" in str(e):
                 time.sleep(3)  # Wait a bit before retrying
                 continue   
             
        except Exception:
            # User blocked bot or other error, just skip
            pass

    bot.send_message(chat_id, f"✅ Announcement sent to {sent_count} users.", reply_markup=get_admin_panel())


# Back to Admin Panel button
# @bot.message_handler(func=lambda message: message.text == "🔙 Back to Admin Panel")
# def back_to_admin_panel(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, "Admin Panel.", reply_markup=get_admin_panel())