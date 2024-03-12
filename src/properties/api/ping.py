from flask import Blueprint, jsonify


bp = Blueprint("ping", __name__, url_prefix="/ping")


@bp.route("/", methods=["GET"])
def register_sale():
    return jsonify({"message": "pong"})
