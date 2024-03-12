from dataclasses import dataclass

from properties.seedwork.application.queries import Query, QueryResult, execute_query as query
from properties.modules.grounds.application.mappers import GroundMapper
from properties.modules.grounds.application.queries.base import BaseQueryHandler


@dataclass
class GetGround(Query):
    id: str


class GetGroundHandler(BaseQueryHandler):

    def handle(self, query: GetGround) -> QueryResult:
        sale = self.repository.get_by_id(query.id)
        mapper = GroundMapper()
        return QueryResult(data=mapper.entity_2_dto(sale))


@query.register(GetGround)
def execute_get_sale(query: GetGround):
    handler = GetGroundHandler()
    return handler.handle(query)
