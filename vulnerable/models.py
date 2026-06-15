from vulnerable.database import get_db

def get_user_by_username(username):
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()
    conn.close()
    return user

def check_password(user, password):
    # Intentionally insecure: plain string compare
    return user['password'] == password

def get_user_by_id(user_id):
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE id = ?", (user_id,)
    ).fetchone()
    conn.close()
    return user

def get_all_posts():
    conn = get_db()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return posts