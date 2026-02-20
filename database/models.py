from database.db import get_connection

from datetime import datetime



# ---- Feedback Table Functions ----

def save_feedback(user_id, username, text):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute ("""
        INSERT INTO feedback (user_id, username, message)
        VALUES(%s, %s, %s)
    """, (user_id, username, text))

    conn.commit()
    conn.close()


def get_user_feedbacks(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT message, created_at
        FROM feedback
        WHERE user_id = %s
        ORDER BY created_at DESC
    """, (user_id,)
    )
    data = cursor.fetchall()
    conn.close()
    return data


def get_all_feedbacks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, username, message, created_at
        FROM feedback
        ORDER BY created_at DESC
    """)

    data = cursor.fetchall()
    conn.close()

    return data




# ---- Users Table Functions ----

def save_user(user_id, username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (user_id, username)
        VALUES (%s, %s)
        ON CONFLICT (user_id) DO NOTHING
    """, (user_id, username)
    )

    conn.commit()
    conn.close()



def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()

    conn.close()

    return users


# Resetting the database every new year

def reset_database_if_new_year():
    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now()
    current_year = str(now.year)

    # Check if reset already happened this year
    cursor.execute("SELECT value FROM settings WHERE key = 'last_reset_year'")
    row = cursor.fetchone()

    if row is None or row[0] != current_year:
        # Only reser if today January 1st
        if now.month == 1 and now.day == 1:
            print("New year detected. Resetting database...")

        # Clear database tables
        cursor.execute("DELETE FROM feedbacks")
        cursor.execute("DELETE FROM users")

        # Save reset year
        cursor.execute("""
            INSERT OR REPLACE INTO settings (key, value)
            VAULES ('last_reset_year', %s)
        """, (current_year))

        conn.commit()
        print("Database reset complete.")