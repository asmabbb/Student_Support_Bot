# import sqlite3
import psycopg2
import os

# DB_NAME = "CETSU_Student_Support.db"
# DB_NAME = os.environ.get('DB_NAME', 'CETSU_Student_Support.db')

DATABASE_URL = os.getenv("DATABASE_URL")




def get_connection():
    return psycopg2.connect(DATABASE_URL)


# ---- Create Feedback & Users Tables in DB ----
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Create Feedback Table:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id SERIAL PRIMARY KEY,
        user_id BIGINT NOT NULL,
        username TEXT,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    

    # Create Users Table:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username TEXT     
                   )
    """)

    conn.commit()
    conn.close()