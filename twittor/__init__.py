from flask import Flask
from twittor.route import index, login
import os

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(32) # A Secret key for preventing CSRF attack, required by WTForms
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=["GET", "POST"])
    return app