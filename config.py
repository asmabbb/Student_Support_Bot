# import os


# API_TOKEN = os.environ['BOT_TOKEN']
# ADMIN_ID = list(map(int, os.environ.get('ADMIN_ID', '').split(',')))
# DB_NAME = os.environ.get('DB_NAME', 'CETSU_Student_Support.db')


import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
#DATABASE_URL = os.getenv("DATABASE_URL")
ADMIN_ID = list(map(int, os.getenv("ADMIN_ID", "").split(","))) if os.getenv("ADMIN_ID") else []