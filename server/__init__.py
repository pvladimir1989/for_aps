from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

app = Flask(__name__)

# app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}

# swagger_config = {
#     "headers": [],
#     "specs": [
#         {
#             "endpoint": "apispec_1",
#             "route": "/apispec_1.json",
#             "rule_filter": lambda rule: True,  # all in
#             "model_filter": lambda tag: True,  # all in
#         }
#     ],
#     "static_url_path": "/flasgger_static",
#     # "static_folder": "static",  # must be set by user
#     "swagger_ui": True,
#     "specs_route": "/swagger/",
# }
# swagger = Swagger(app, template=swagger_config)
swagger = Swagger(app)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from server import app, models
