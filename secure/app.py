from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import CSRFProtect
from secure.models import get_user_by_username, check_password
from secure.forms import LoginForm
from shared.config import SECRET_KEY, SESSION_LIFETIME
import os

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['WTF_CSRF_ENABLED'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = SESSION_LIFETIME

csrf = CSRFProtect(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_username(form.username.data)
        if user and check_password(user, form.password.data):
            session.clear()                        # A07 fix 1: regenerate session
            session.permanent = True               # A07 fix 2: enforce TTL
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('index'))
        form.username.errors.append('Invalid credentials')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))