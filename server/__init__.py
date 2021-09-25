from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from asgiref.wsgi import WsgiToAsgi
from quart import Quart

app = Flask(__name__)
# app = Quart(__name__)
# app.app_context().push()
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from server import app, models
