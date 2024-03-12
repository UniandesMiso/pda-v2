from dataclasses import dataclass

from properties.seedwork.application.commands import Command, CommandResult, execute_command as command
from properties.modules.grounds.application.dto import GroundDTO
from properties.modules.grounds.application.mappers import GroundMapper
from properties.modules.grounds.application.commands.base import BaseCommandHandler


@dataclass
class UpdateGroundDimension(Command):
    id: str
    width: float
    length: float

class UpdateGroundDimensionHandler(BaseCommandHandler):

    def handle(self, command: UpdateGroundDimension) -> CommandResult:
        ground_dto = GroundDTO(
            id=command.id,
            width=command.width,
            length=command.length,
        )

        mapper = GroundMapper()
        ground = mapper.dto_2_entity(ground_dto)

        self.repository.update(ground)
        return CommandResult(data=mapper.entity_2_dto(ground))


@command.register(UpdateGroundDimension)
def execute_update_ground_status(command: UpdateGroundDimension):
    handler = UpdateGroundDimensionHandler()
    return handler.handle(command)
