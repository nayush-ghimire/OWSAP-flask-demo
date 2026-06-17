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

def get_user_posts(user_id):
    conn = get_db()
    posts = conn.execute(
        "SELECT * FROM posts WHERE user_id = ?", (user_id,)
    ).fetchall()
    conn.close()
    return posts

def search_posts_vulnerable(query):
    conn = get_db()

    # A03 - SQL Injection vulnerability
    sql = f"SELECT * FROM posts WHERE title LIKE '%{query}%'"

    posts = conn.execute(sql).fetchall()
    conn.close()
    return posts