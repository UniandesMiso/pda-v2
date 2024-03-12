from flask import Blueprint, jsonify, request

from listings.seedwork.application.commands import execute_command
from listings.modules.information.application.mappers import ListingMapperDTO
from listings.modules.information.application.commands.process_listing import ProcessInformation

bp = Blueprint("information", __name__, url_prefix="/information")


@bp.route("/", methods=["POST"])
def process_information():
    mapper = ListingMapperDTO()
    listing_dto = mapper.dict_2_dto(request.json)

    command = ProcessInformation(properties=listing_dto.properties)
    result = execute_command(command)

    return jsonify(mapper.dto_2_dict(result.data))
