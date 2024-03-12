from uuid import uuid4
from dataclasses import dataclass

from properties.config.db import db
from properties.seedwork.application.commands import Command, CommandResult, execute_command as command
from properties.modules.grounds.application.dto import GroundDTO
from properties.modules.grounds.application.mappers import GroundMapper
from properties.modules.grounds.application.commands.base import BaseCommandHandler


@dataclass
class RegisterGround(Command):
    address: str
    location: str

class RegisterGroundHandler(BaseCommandHandler):

    def handle(self, command: RegisterGround) -> CommandResult:
        ground_dto = GroundDTO(
            id=str(uuid4()),
            address=command.address,
            location=command.location,
        )

        mapper = GroundMapper()
        ground = mapper.dto_2_entity(ground_dto)

        self.repository.create(ground)
        return CommandResult(data=mapper.entity_2_dto(ground))


@command.register(RegisterGround)
def execute_register_sale(command: RegisterGround):
    handler = RegisterGroundHandler()
    return handler.handle(command)
