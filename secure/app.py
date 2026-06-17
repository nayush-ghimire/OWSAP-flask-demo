from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    abort,
)

from flask_wtf import CSRFProtect

from secure.models import (
    get_user_by_username,
    check_password,
    get_user_by_id,
    get_user_posts,
    search_posts_secure,
)

from secure.forms import LoginForm
from shared.config import SECRET_KEY, SESSION_LIFETIME

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
            session.clear()          
            session.permanent = True 

            session['user_id'] = user['id']
            session['username'] = user['username']

            return redirect(url_for('index'))

        form.username.errors.append('Invalid credentials')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# IDOR Fix

@app.route('/profile')
def profile():
    user_id = request.args.get('id')

    if (
        not session.get('user_id')
        or str(session['user_id']) != str(user_id)
    ):
        abort(403)

    user = get_user_by_id(user_id)
    posts = get_user_posts(user_id)

    return render_template(
        'profile.html',
        user=user,
        posts=posts
    )


# SQL Injection Fix

@app.route('/search')
def search():
    query = request.args.get('q', '')

    results = (
        search_posts_secure(query)
        if query else []
    )

    return render_template(
        'search.html',
        results=results,
        query=query
    )