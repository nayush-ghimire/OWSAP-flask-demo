
SEED_USERS = [
    {"id": 1, "username": "admin",   "password": "admin123",    "role": "admin"},
    {"id": 2, "username": "alice",   "password": "password1",   "role": "user"},
    {"id": 3, "username": "bob",     "password": "hunter2",     "role": "user"},
]

SEED_POSTS = [
    {"id": 1, "user_id": 1, "title": "Welcome",        "body": "This is the admin welcome post."},
    {"id": 2, "user_id": 2, "title": "Alice's Post",   "body": "Hello from Alice!"},
    {"id": 3, "user_id": 3, "title": "Bob's Post",     "body": "Hello from Bob!"},
]