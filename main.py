from bot_instance import bot

import handlers.main_menu
import handlers.feedback

from database.db import create_tables

create_tables()

bot.infinity_polling()
