import os

basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import load_dotenv
load_dotenv()

# from dotenv import load_dotenv

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    print(SQLALCHEMY_DATABASE_URI, '777')
    # SQLALCHEMY_DATABASE_URI = "postgresql://local:local@localhost/local"
    SQLALCHEMY_DATABASE_URI = "postgresql://db:postgres@localhost:5432/posts"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
