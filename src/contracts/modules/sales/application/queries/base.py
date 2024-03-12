from contracts.seedwork.application.queries import QueryHandler
from contracts.modules.sales.infrastructure.repositories import SaleRepositoryGeneric


class BaseQueryHandler(QueryHandler):

    def __init__(self):
        self._repository = SaleRepositoryGeneric()

    @property
    def repository(self):
        return self._repository
