import sqlite3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared.config import VULNERABLE_DB_PATH
from shared.seed_data import SEED_USERS, SEED_POSTS

VULN_DB = VULNERABLE_DB_PATH 

def get_db():
    conn = sqlite3.connect(VULN_DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            body TEXT
        );
    """)
    # Plaintext passwords which are intentionally insecure
    for u in SEED_USERS:
        cur.execute(
            "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
            (u['username'], u['password'])  # raw string, no hashing
        )
    for p in SEED_POSTS:
        cur.execute(
            "INSERT OR IGNORE INTO posts (user_id, title, body) VALUES (?, ?, ?)",
            (p['user_id'], p['title'], p['body'])
        )
    conn.commit()
    conn.close()
    print(f"[vulnerable] DB initialized at {VULN_DB}")