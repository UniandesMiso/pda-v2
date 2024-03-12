from os import environ
from flask import Flask

from bff.config import config
from bff.api.v1 import bp as v1_bp


def create_app():
    config_name = environ.get("FLASK_CONFIG", "development")
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    init_api(app)
    return app


def init_api(app):
    app.register_blueprint(v1_bp)
