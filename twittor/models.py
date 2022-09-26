from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from twittor import db, login_manager
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash=db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    tweets = db.relationship("Tweet", backref='author', lazy='dynamic')

    def __repr__(self):
        return f'id={self.id}, username={self.username}, password_hash={self.password_hash}, email={self.email}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
        return User.query.get(int(id))

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'id={self.id}, tweet={self.body}, create_time={self.create_time}, user_id={self.user_id}'