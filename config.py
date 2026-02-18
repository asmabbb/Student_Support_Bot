import os


API_TOKEN = os.environ['BOT_TOKEN']
ADMIN_ID = list(map(int, os.environ.get('ADMIN_ID', '').split(',')))
DB_NAME = os.environ.get('DB_NAME', 'CETSU_Student_Support.db')