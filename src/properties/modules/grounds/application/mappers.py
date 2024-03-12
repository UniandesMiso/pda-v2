from uuid import UUID

from properties.seedwork.application.dto import Mapper as ApplicationMapper
from properties.seedwork.domain.repositories import Mapper as RepositoryMapper
from properties.seedwork.domain.entities import Dimension, Amount
from properties.modules.grounds.application.dto import GroundDTO
from properties.modules.grounds.domain.entities import Ground


class GroundMapperDTO(ApplicationMapper):

    def dict_2_dto(self, dict: dict) -> GroundDTO:
        ground_dto = GroundDTO(
            id=dict.get("id"),
            createdAt=dict.get("createdAt"),
            updatedAt=dict.get("updatedAt"),
            address=dict.get("address"),
            width=dict.get("width"),
            length=dict.get("length"),
            location=dict.get("location"),
            price=dict.get("price"),
            currency=dict.get("currency")
        )
        return ground_dto

    def dto_2_dict(self, dto: GroundDTO, role: str = "QUERY") -> dict:
        ground_dict =  dto.__dict__
        if role == "AGENCY":
            ground_dict.pop("price")
            ground_dict.pop("currency")
        return ground_dict


class GroundMapper(RepositoryMapper):

    def get_type(self) -> type:
        return Ground.__class__

    def entity_2_dto(self, entity: Ground) -> GroundDTO:
        ground_dto = GroundDTO(
            id=entity.id,
            createdAt=entity.created_at.strftime("%d/%m/%Y %I:%M %p"),
            updatedAt=entity.updated_at.strftime("%d/%m/%Y %I:%M %p"),
            address=entity.address,
            width=entity.dimension.width,
            length=entity.dimension.length,
            location=entity.location,
            price=entity.amount.price,
            currency=entity.amount.currency
        )
        return ground_dto

    def dto_2_entity(self, dto: GroundDTO) -> Ground:
        ground = Ground()
        ground.id = UUID(dto.id)
        ground.address = dto.address
        ground.dimension = Dimension(width=dto.width, length=dto.length)
        ground.location = dto.location       
        ground.amount = Amount(price=dto.price, currency=dto.currency)
        return ground
