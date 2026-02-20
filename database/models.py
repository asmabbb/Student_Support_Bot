from database.db import get_connection



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