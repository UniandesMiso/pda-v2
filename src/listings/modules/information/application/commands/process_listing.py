from uuid import uuid4
from dataclasses import dataclass
from pydispatch import dispatcher

from listings.seedwork.application.commands import Command, CommandResult, execute_command as command
from listings.modules.information.application.dto import ListingDTO, PropertyDTO
from listings.modules.information.application.mappers import ListingMapper
from listings.modules.information.application.commands.base import BaseCommandHandler


@dataclass
class Property:
    id: str
    width: float
    length: float


@dataclass
class ProcessInformation(Command):
    properties: list[Property]


class ProcessInformationHandler(BaseCommandHandler):

    def handle(self, command: ProcessInformation) -> CommandResult:
        property_dtos = []
        for property in command.properties:
            property_dto = PropertyDTO(
                id=property.id,
                width=property.width,
                length=property.length,
            )
            property_dtos.append(property_dto)

        listing_dto = ListingDTO(
            id=str(uuid4()),
            properties=property_dtos,
        )

        mapper = ListingMapper()
        listing = mapper.dto_2_entity(listing_dto)
        listing.process_properties()

        for event in listing.events:
            dispatcher.send(event=event, signal=type(event).__name__)

        return CommandResult(data=mapper.entity_2_dto(listing))


@command.register(ProcessInformation)
def execute_register_sale(command: ProcessInformation):
    handler = ProcessInformationHandler()
    return handler.handle(command)
