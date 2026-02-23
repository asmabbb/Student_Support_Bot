from bot_instance import bot
from config import ADMIN_ID
from keyboards import main_keyboard
from keyboards import feedback_keyboard
from keyboards import admin_panel_keyboard
from database.models import save_feedback, get_user_feedbacks

from database.models import save_feedback


feedback_mode_users = set()

# creating the menu option response handler:
@bot.message_handler(content_types=["text"], func=lambda message: message.text in ['🤖 CETSU Bots', '📢 Announcements & Group Chats', '📥 Feedback', '⚙️ Admin Panel'])
def option_handler(message):
    option = message.text
    chat_id = message.chat.id

    if option == "🤖 CETSU Bots":
        bot.send_message(chat_id, "These are the CET Student Union bots: ", reply_markup=main_keyboard.bots_menu)


    elif option == "📥 Feedback":
        bot.send_message(chat_id, "قسم الملاحظات.", reply_markup=feedback_keyboard.feedback_menu_keyboard())


    elif option == "📢 Announcements & Group Chats":
        bot.send_message(chat_id, "إطَّلع على آخر الأخبار, وانضم لمجموعة الطلبة العامة من هنا:", reply_markup=main_keyboard.join_us_menu)


    elif option == "⚙️ Admin Panel":
        bot.send_message(chat_id, "Admin Panel:", reply_markup=admin_panel_keyboard.get_admin_panel())
        


# Handle Feedback Section 
@bot.message_handler(func=lambda message: message.text in ["✍️ Submit Feedback", "📂 View My Feedback", "🔙 Back to Main Menu"] )
def make_feedback(message):
    chat_id = message.chat.id
    option = message.text

    # ---- [✍️ Submit Feedback] Button ----
    if option == "✍️ Submit Feedback":
        feedback_mode_users.add(chat_id)
        bot.send_message(chat_id, "أنت الآن في وضع إرسال الملاحظات, يرجى كتابة ملاحظتك, أو كتابة /cancel للإلغاء.")
        bot.register_next_step_handler(message, process_feedback)


    # ---- [📂 View My Feedback] Button ----
    elif option == "📂 View My Feedback":
        feedbacks = get_user_feedbacks(message.from_user.id)

        if not feedbacks:
            bot.send_message(message.chat.id, "📭 لم تقم بإرسال أي ملاحظات حتى الآن.")
            return
        
        text = ""
        for fb in feedbacks:
            formatted_date = fb[1].strftime(("%Y-%m-%d at %I:%M %p"))
            text += f"📝 {fb[0]}\n\n📅 {formatted_date}\n\n----------------------------------------------------------\n"

        bot.send_message(message.chat.id, text)


    # ---- [🔙 Back to Main Menu] Button ----
    elif option == "🔙 Back to Main Menu":
        is_admin = message.from_user.id in ADMIN_ID
        bot.send_message(message.chat.id, "🔙 تم الرجوع إلى القائمة الرئيسية.", reply_markup=main_keyboard.main_menu(is_admin))






def process_feedback(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.from_user.username
    text = message.text
    
    if chat_id not in feedback_mode_users:
        return
    
    if message.text == "/cancel":
        feedback_mode_users.remove(chat_id)
        bot.send_message(chat_id, "تم إلغاء وضع Feedback mode.")
        return
    
    if text.startswith("/") or text in ["✍️ Submit Feedback", "📂 View My Feedback", "🔙 Back to Main Menu"]:
        bot.send_message(chat_id, "⚠️ أنت حالياً في وضع Feedback mode. \nيرجى كتابة ملاحظتك,أو كتابة /cancel للإلغاء و الخروج من هذا الوضع.")
        bot.register_next_step_handler(message, process_feedback)
        return
    
    save_feedback(user_id, username, text)
    
    bot.reply_to(message, "✅ تم استلام ملاحظتك بنجاح، وسيتم مراجعتها في أقرب وقت ممكن. \nنشكرك على تواصلك ومساهمتك القيّمة.")
    feedback_mode_users.remove(chat_id)


# View My Feedback
# @bot.message_handler(func=lambda message: message.text == "📂 View My Feedback")
# def view_my_feedback(message):
    
#     feedbacks = get_user_feedbacks(message.from_user.id)

#     if not feedbacks:
#         bot.send_message(message.chat.id, "You haven't submitted any feedbacks yet.")
#         return
    
#     text = ""
#     for fb in feedbacks:
#         formatted_date = fb[1].strftime(("%Y-%m-%d at %I:%M %p"))
#         text += f"📝 {fb[0]}\n\n📅 {formatted_date}\n\n----------------------------------------------------------\n"

#     bot.send_message(message.chat.id, text)


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
# @bot.message_handler(func=lambda message: message.text == "🔙 Back to Main Menu")
# def back_to_main(message):
#     is_admin = message.from_user.id in ADMIN_ID
#     bot.send_message(message.chat.id, "Welcom back the main menu!", reply_markup=main_keyboard.main_menu(is_admin))

