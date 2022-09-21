import os

config_path = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.urandom(32) # A Secret key for preventing CSRF attack, required by WTForms
    # By use a env path "DATABASE_URI", custom path can be specified.
    # If "DATABASE_URI" is not specified, use the second path
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///" + os.path.join(config_path, "twitter.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False