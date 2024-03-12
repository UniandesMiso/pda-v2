from logging import error
from dataclasses import dataclass
from pydispatch import dispatcher

from properties.seedwork.application.commands import Command, CommandResult, execute_command as command
from properties.modules.grounds.application.dto import GroundDTO
from properties.modules.grounds.application.mappers import GroundMapper
from properties.modules.grounds.application.commands.base import BaseCommandHandler
from properties.modules.grounds.domain.events import AmountUpdateFailed


@dataclass
class UpdateAmount(Command):
    property_id: str
    sale_id: str
    price: float
    currency: str


class UpdateAmountHandler(BaseCommandHandler):

    def handle(self, command: UpdateAmount) -> CommandResult:
        try:
            # raise Exception("Simulated fail")
        
            ground_dto = GroundDTO(
                id=command.property_id,
                price=command.price,
                currency=command.currency
            )

            mapper = GroundMapper()
            ground = mapper.dto_2_entity(ground_dto)

            ground.update_amount(sale_id=command.sale_id)
            self.repository.update(ground)

            for event in ground.events:
                dispatcher.send(event=event, signal=type(event).__name__)

            return CommandResult(data=mapper.entity_2_dto(ground))
        except Exception as ex:
            error(str(ex))

            event = AmountUpdateFailed(
                sale_id=command.sale_id,
                property_id=command.property_id,
                price=command.price,
                currency=command.currency,
            )

            dispatcher.send(event=event, signal=type(event).__name__)


@command.register(UpdateAmount)
def execute_update_ground_status(command: UpdateAmount):
    handler = UpdateAmountHandler()
    return handler.handle(command)
