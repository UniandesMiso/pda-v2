from dataclasses import dataclass

from contracts.seedwork.application.commands import Command, CommandResult, execute_command as command
from contracts.modules.sales.application.commands.base import BaseCommandHandler


@dataclass
class DeleteSale(Command):
    id: str


class DeleteSaleHandler(BaseCommandHandler):

    def handle(self, command: DeleteSale) -> CommandResult:
        self.repository.delete(command.id)
        return CommandResult(data=None)


@command.register(DeleteSale)
def execute_register_sale(command: DeleteSale):
    handler = DeleteSaleHandler()
    return handler.handle(command)
