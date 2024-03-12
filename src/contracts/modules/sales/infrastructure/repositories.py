from uuid import UUID
from datetime import datetime

from contracts.config.db import db
from contracts.modules.sales.domain.entities import Sale
from contracts.modules.sales.domain.repositories import SaleRepository
from contracts.modules.sales.domain.rules import PriceRequired
from contracts.modules.sales.infrastructure.mappers import SaleMapper
from contracts.modules.sales.infrastructure.dto import Sale as SaleDTO


class SaleRepositoryGeneric(SaleRepository):

    def create(self, entity: Sale):
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        entity.validate_rule(PriceRequired(entity))
        mapper = SaleMapper()
        sale_dto = mapper.entity_2_dto(entity)
        db.session.add(sale_dto)
        db.session.commit()

    def get_by_id(self, id: UUID) -> Sale:
        sale_dto = db.session.query(SaleDTO).get(id)
        mapper = SaleMapper()
        sale = mapper.dto_2_entity(sale_dto)
        return sale
    
    def delete(self, id: UUID):
        sale_dto = db.session.query(SaleDTO).get(id)
        db.session.delete(sale_dto)
        db.session.commit()
