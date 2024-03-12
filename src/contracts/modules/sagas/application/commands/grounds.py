from uuid import uuid4
from dataclasses import dataclass

from contracts.seedwork.application.commands import Command, CommandHandler, execute_command as command
from contracts.modules.sagas.infrastructure.dispatchers import Dispatcher
from contracts.modules.sagas.infrastructure.utils import time_millis


@dataclass
class UpdateAmount(Command):
    property_id: str
    sale_id: str
    price: float
    currency: str


class UpdateAmountHandler(CommandHandler):

    def handle(self, command: UpdateAmount):
        data = dict(
            propertyId=command.property_id,
            saleId=command.sale_id,
            price=command.price,
            currency=command.currency,
        )

        message = dict(id=str(uuid4()), ingestion=time_millis(), data=data)
        dispatcher = Dispatcher()
        dispatcher.send_message(message, "update-amount-command")



@command.register(UpdateAmount)
def execute_update_amount(command: UpdateAmount):
    handler = UpdateAmountHandler()
    return handler.handle(command)
