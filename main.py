from bot_instance import bot

import handlers.main_menu
import handlers.feedback
import handlers.admin_panel
import handlers.fallback

from database.db import create_tables

# ----- Flask Server -----
from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "CETSU Student Support Bot is alive!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# Start web server in seperate thread
threading.Thread(target=run_web).start()

# ---- Start Everything ---- 
create_tables()

bot.infinity_polling(timeout=10, long_polling_timeout=5)
