from bot_instance import bot

import handlers.main_menu
import handlers.feedback

from database.db import create_tables


# ----- Flask Keep-alive server -----
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "CETSU Student Support bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


# ---- Start Everything ---- 
create_tables()

bot.infinity_polling()
