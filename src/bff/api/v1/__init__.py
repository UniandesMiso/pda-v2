from os import path
from flask import Blueprint, request, jsonify, current_app
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, ObjectType
from ariadne.explorer import ExplorerGraphiQL

from bff.api.v1.queries import get_ground_query
from bff.api.v1.mutations import create_ground_mutation, create_sale_mutation, process_listing_mutation


bp = Blueprint("v1", __name__, url_prefix="/v1")

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("getGround", get_ground_query)
mutation.set_field("createGround", create_ground_mutation)
mutation.set_field("createSale", create_sale_mutation)
mutation.set_field("processListing", process_listing_mutation)

basedir = path.abspath(path.dirname(__file__))
type_defs = load_schema_from_path(path.join(basedir, "schema.graphql"))
schema = make_executable_schema(type_defs, query, mutation)
explorer_html = ExplorerGraphiQL().html(None)


@bp.route("/ping", methods=["GET"])
def register_sale():
    return jsonify({"message": "pong"})


@bp.route("/graphql", methods=["GET"])
def graphql_playground():
    return explorer_html, 200


@bp.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=current_app.debug,
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
