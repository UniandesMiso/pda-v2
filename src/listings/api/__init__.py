from os import environ
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from listings.config import config
from listings.config.db import init_db
from contracts.api.ping import bp as ping_bp
from listings.api.information import bp as listings_bp


def create_app():
    config_name = environ.get("FLASK_CONFIG", "development")

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_error_handler(HTTPException, exception_handler)

    init_db(app)
    init_api(app)

    return app


def init_api(app):
    app.register_blueprint(ping_bp)
    app.register_blueprint(listings_bp)


def exception_handler(ex: HTTPException):
    return jsonify({"message": ex.description}), ex.code
