from flask import Blueprint, jsonify, request

from contracts.seedwork.application.queries import execute_query
from contracts.seedwork.application.commands import execute_command
from contracts.modules.sales.application.mappers import SaleMapperDTO
from contracts.modules.sales.application.queries.get_sale import GetSale
from contracts.modules.sales.application.commands.register_sale import RegisterSale


bp = Blueprint("sales", __name__, url_prefix="/sales")


@bp.route("/", methods=["POST"])
def register_sale():
    mapper = SaleMapperDTO()
    sale_dto = mapper.dict_2_dto(request.json)

    command = RegisterSale(
        property_id=sale_dto.propertyId,
        price=sale_dto.price,
        currency=sale_dto.currency,
        executed_at=sale_dto.executedAt,
    )

    result = execute_command(command)
    return jsonify(mapper.dto_2_dict(result.data))


@bp.route("/<id>", methods=["GET"])
def get_sale(id=None):
    if not id:
        return jsonify({"message": "The sale ID is required"}), 400

    query = GetSale(id=id)
    result = execute_query(query)

    mapper = SaleMapperDTO()
    return jsonify(mapper.dto_2_dict(result.data))
