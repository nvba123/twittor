from flask import render_template, redirect, url_for
from twittor.forms import LoginForm
from twittor.models import User, Tweet

def index():
    name = {"username": "root"}
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
    return render_template("index.html", name=name, posts=posts)

def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("index"))

    return render_template("login.html", form=form)