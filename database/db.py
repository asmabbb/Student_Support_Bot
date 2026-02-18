# import sqlite3
import psycopg2
import os

# DB_NAME = "CETSU_Student_Support.db"
# DB_NAME = os.environ.get('DB_NAME', 'CETSU_Student_Support.db')

DATABASE_URL = os.getenv("DATABASE_URL")




def get_connection():
    return psycopg2.connect(DATABASE_URL)



def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id BIGINT NOT NULL,
        username TEXT,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()
