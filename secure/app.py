import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask
from shared.config import SECRET_KEY, SESSION_LIFETIME

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.permanent_session_lifetime = SESSION_LIFETIME

@app.route("/")
def index():
    return "Secure app is running."