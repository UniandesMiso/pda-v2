from os import environ
from threading import Thread
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from contracts.config import config
from contracts.config.db import init_db
from contracts.api.ping import bp as ping_bp
from contracts.api.sales import bp as sales_bp

import contracts.modules.sales.infrastructure.consumers as sales_consumers
import contracts.modules.sagas.infrastructure.consumers as sagas_consumers


def create_app():
    config_name = environ.get("FLASK_CONFIG", "development")

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_error_handler(HTTPException, exception_handler)

    init_db(app)
    init_api(app)
    # init_consumers(app)

    return app


def init_api(app):
    app.register_blueprint(ping_bp)
    app.register_blueprint(sales_bp)


def init_consumers(app):
    Thread(target=sales_consumers.subscribe_2_register_sale_command, args=[app]).start()
    Thread(target=sagas_consumers.subscribe_2_ground_events, args=[app]).start()
    Thread(target=sagas_consumers.subscribe_2_ground_errors_events, args=[app]).start()


def exception_handler(ex: HTTPException):
    return jsonify({"message": ex.description}), ex.code
