# 🎓 CETSU Student Support Bot

A Telegram bot designed to help students of the College of Electronic Technologies quickly access essential resources, official channels, and student support services.

---

## Features

### Main Menu

The bot provides a structured main menu with the following options:

1. **CET Student Union Bots**
   - A list of official CETSU bots that assist students with different services.

2. **Announcements & Group Chats**
   - Direct access to official CETSU announcement channels and student group chats.

3. **Feedback System**
   - Students can submit feedback directly through the bot.
   - Users can view their own submitted feedback (if available).
   - Admins can view all submitted feedback with a single click.

---

## Database

The feedback system is powered by **SQLite3**, allowing:

- Storage of user ID
- Username tracking
- Feedback message
- Automatic timestamp (created_at)
- Ordered retrieval (latest first)

---

## Technologies Used

- Python
- pyTelegramBotAPI (Telebot)
- SQLite3
- Telegram Bot API (Reply & Inline Keyboards)

---

## Admin Capabilities

- View all student feedback
- Access restricted via admin ID check

---

## Deployment

The bot can be deployed using platforms such as:
- Railway
- Render
- PythonAnywhere

Environment variables should be used to securely store the bot token.

---

## Future Improvements

- Categorized feedback (Complaint / Lost / Found)
- Media support (photo submissions)
- Enhanced admin moderation tools

---

## Project Status

Fully functional and ready for deployment.
