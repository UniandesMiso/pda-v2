from contracts.seedwork.domain.repositories import Mapper
from contracts.seedwork.domain.entities import Amount
from contracts.modules.sales.domain.entities import Sale
from contracts.modules.sales.infrastructure.dto import Sale as SaleDTO


class SaleMapper(Mapper):

    def get_type(self) -> type:
        return Sale.__class__

    def entity_2_dto(self, entity: Sale) -> SaleDTO:
        sale_dto = SaleDTO()
        sale_dto.id = str(entity.id)
        sale_dto.property_id = entity.property_id
        sale_dto.created_at = entity.created_at
        sale_dto.updated_at = entity.updated_at
        sale_dto.price = entity.amount.price
        sale_dto.currency = entity.amount.currency
        sale_dto.executed_at = entity.executed_at
        return sale_dto

    def dto_2_entity(self, dto: SaleDTO) -> Sale:
        sale = Sale()
        sale.id = dto.price
        sale.property_id = dto.property_id
        sale.created_at = dto.created_at
        sale.updated_at = dto.updated_at
        sale.amount = Amount(price=dto.price, currency=dto.currency)
        sale.created_at = dto.created_at
        return sale
