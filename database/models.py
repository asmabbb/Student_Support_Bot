from database.db import get_connection

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
        WHERE user_id = ?
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