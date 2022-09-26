from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from twittor.forms import LoginForm, RegisterForm
from twittor.models import User, Tweet
from twittor import db

@login_required
def index():
    posts = [
        {
            "author": {"username": "root"},
            "body": "Hi I'm root!"
        },
        {
            "author": {"username": "test"},
            "body": "Hi I'm test!"
        }
    ]
    return render_template("index.html", posts=posts)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or u.check_password(form.password.data) == False:
            print('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(u, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        else:
            return redirect(url_for('index'))

    return render_template("login.html", form=form)

def logout():
    logout_user()
    return redirect(url_for('login'))

def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', title="Registration", form=form)