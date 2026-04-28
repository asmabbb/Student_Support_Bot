from bot_instance import bot

import handlers.main_menu
import handlers.feedback
import handlers.admin_panel
import handlers.announcements
import handlers.fallback

from database.db import create_tables
from database.models import reset_database_if_new_year

# ---- Start Everything ---- 
create_tables()

reset_database_if_new_year()

print("Starting Student Support Bot (polling mode)...")

bot.infinity_polling(timeout=10, long_polling_timeout=5)