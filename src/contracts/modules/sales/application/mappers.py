from uuid import UUID
from datetime import datetime

from contracts.seedwork.application.dto import Mapper as ApplicationMapper
from contracts.seedwork.domain.repositories import Mapper as RepositoryMapper
from contracts.seedwork.domain.entities import Amount
from contracts.modules.sales.application.dto import SaleDTO
from contracts.modules.sales.domain.entities import Sale


class SaleMapperDTO(ApplicationMapper):

    def dict_2_dto(self, dict: dict) -> SaleDTO:
        sale_dto = SaleDTO(
            id=dict.get("id"),
            propertyId=dict.get("propertyId"),
            createdAt=dict.get("createdAt"),
            updatedAt=dict.get("updatedAt"),
            price=dict.get("price"),
            currency=dict.get("currency"),
            executedAt=dict.get("executedAt"),
        )
        return sale_dto

    def dto_2_dict(self, dto: SaleDTO) -> dict:
        return dto.__dict__


class SaleMapper(RepositoryMapper):

    def get_type(self) -> type:
        return Sale.__class__

    def entity_2_dto(self, entity: Sale) -> SaleDTO:
        sale_dto = SaleDTO(
            id=entity.id,
            propertyId=entity.property_id,
            createdAt=entity.created_at.strftime("%d/%m/%Y %I:%M %p"),
            updatedAt=entity.updated_at.strftime("%d/%m/%Y %I:%M %p"),
            price=entity.amount.price,
            currency=entity.amount.currency,
            executedAt=entity.executed_at.strftime("%d/%m/%Y"),
        )
        return sale_dto

    def dto_2_entity(self, dto: SaleDTO) -> Sale:
        sale = Sale()
        sale.id = UUID(dto.id)
        sale.property_id = dto.propertyId
        sale.amount = Amount(price=dto.price, currency=dto.currency)
        sale.executed_at = datetime.strptime(dto.executedAt, "%d/%m/%Y")
        return sale
