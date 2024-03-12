from properties.seedwork.application.queries import QueryHandler
from properties.modules.grounds.infrastructure.repositories import GroundRepositorySQL


class BaseQueryHandler(QueryHandler):

    def __init__(self):
        self._repository = GroundRepositorySQL()

    @property
    def repository(self):
        return self._repository
