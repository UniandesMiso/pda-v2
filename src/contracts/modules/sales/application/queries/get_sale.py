from dataclasses import dataclass

from contracts.seedwork.application.queries import Query, QueryResult, execute_query as query
from contracts.modules.sales.application.mappers import SaleMapper
from contracts.modules.sales.application.queries.base import BaseQueryHandler


@dataclass
class GetSale(Query):
    id: str


class GetSaleHandler(BaseQueryHandler):

    def handle(self, query: GetSale) -> QueryResult:
        sale = self.repository.get_by_id(query.id)
        mapper = SaleMapper()
        return QueryResult(data=mapper.entity_2_dto(sale))


@query.register(GetSale)
def execute_get_sale(query: GetSale):
    handler = GetSaleHandler()
    return handler.handle(query)
