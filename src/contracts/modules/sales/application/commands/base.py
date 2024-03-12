from contracts.seedwork.application.commands import CommandHandler
from contracts.modules.sales.infrastructure.repositories import SaleRepositoryGeneric


class BaseCommandHandler(CommandHandler):

    def __init__(self):
        self._repository = SaleRepositoryGeneric()

    @property
    def repository(self):
        return self._repository
