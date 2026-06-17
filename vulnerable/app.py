from flask import Flask, render_template, request, redirect, url_for, session

from vulnerable.models import (
    get_user_by_username,
    check_password,
    get_user_by_id,
    get_user_posts,
    search_posts_vulnerable,
)

from shared.config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user_by_username(username)

        if user and check_password(user, password):
            session['user_id'] = user['id']
            session['username'] = user['username']

            # A07 flaw 1: no session expiry set
            # A07 flaw 2: session ID not regenerated on login

            return redirect(url_for('index'))

        error = 'Invalid credentials'

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/profile')
def profile():
    # No authorization check
    user_id = request.args.get('id')

    user = get_user_by_id(user_id)
    posts = get_user_posts(user_id)

    return render_template(
        'profile.html',
        user=user,
        posts=posts
    )



@app.route('/search')
def search():
    query = request.args.get('q', '')

    results = (
        search_posts_vulnerable(query)
        if query else []
    )

    return render_template(
        'search.html',
        results=results,
        query=query
    )