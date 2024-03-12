from properties.seedwork.domain.repositories import Mapper
from properties.seedwork.domain.value_objects import Dimension, Amount
from properties.modules.grounds.domain.entities import Ground
from properties.modules.grounds.infrastructure.dto import Ground as GroundDTO


class GroundMapper(Mapper):

    def get_type(self) -> type:
        return Ground.__class__

    def entity_2_dto(self, entity: Ground) -> GroundDTO:
        ground_dto = GroundDTO()
        ground_dto.id = str(entity.id)
        ground_dto.created_at = entity.created_at
        ground_dto.updated_at = entity.updated_at
        ground_dto.address = entity.address
        ground_dto.width = entity.dimension.width
        ground_dto.length = entity.dimension.length
        ground_dto.location = entity.location
        ground_dto.price = entity.amount.price
        ground_dto.currency = entity.amount.currency
        return ground_dto

    def dto_2_entity(self, dto: GroundDTO) -> Ground:
        ground = Ground()
        ground.id = dto.id
        ground.created_at = dto.created_at
        ground.updated_at = dto.updated_at
        ground.address = dto.address
        ground.dimension = Dimension(width=dto.width, length=dto.length)
        ground.location = dto.location
        ground.amount = Amount(price=dto.price, currency=dto.currency)
        return ground
