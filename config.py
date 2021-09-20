import os

basedir = os.path.abspath(os.path.dirname(__file__))

# from dotenv import load_dotenv

class Config(object):
    # ...
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = "postgresql://local:local@localhost/local"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
