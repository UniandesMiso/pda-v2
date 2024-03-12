from properties.seedwork.application.commands import CommandHandler
from properties.modules.grounds.infrastructure.repositories import GroundRepositorySQL


class BaseCommandHandler(CommandHandler):

    def __init__(self):
        self._repository = GroundRepositorySQL()

    @property
    def repository(self):
        return self._repository
