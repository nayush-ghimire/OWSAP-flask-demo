import os
from datetime import timedelta

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-in-prod")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VULNERABLE_DB_PATH = os.path.join(BASE_DIR, "vulnerable.db")
SECURE_DB_PATH     = os.path.join(BASE_DIR, "secure.db")

SESSION_LIFETIME = timedelta(minutes=30)