from database.db import get_connection

def save_feedback(user_id, username, text):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute ("""
        INSERT INTO feedback (user_id, username, message)
        VALUES(?, ?, ?)
    """, (user_id, username, text))

    conn.commit()
    conn.close()