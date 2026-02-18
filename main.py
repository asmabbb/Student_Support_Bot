from bot_instance import bot

import handlers.main_menu
import handlers.feedback

from database.db import create_tables



# ---- Start Everything ---- 
create_tables()

bot.infinity_polling(timeout=10, long_polling_timeout=5)
