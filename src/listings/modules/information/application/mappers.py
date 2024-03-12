from uuid import UUID

from listings.seedwork.application.dto import Mapper as ApplicationMapper
from listings.seedwork.domain.value_objects import Property
from listings.seedwork.domain.repositories import Mapper as RepositoryMapper
from listings.modules.information.application.dto import ListingDTO, PropertyDTO
from listings.modules.information.domain.entities import GenericListing


class ListingMapperDTO(ApplicationMapper):

    def dict_2_dto(self, dict: dict) -> ListingDTO:
        property_dtos = []
        for property in dict.get("properties", []):
            property_dto = PropertyDTO(
                id=property.get("id"),
                width=property.get("width"),
                length=property.get("length"),
            )
            property_dtos.append(property_dto)

        listing_dto = ListingDTO(
            id=dict.get("id"),
            properties=property_dtos,
            createdAt=dict.get("createdAt"),
            updatedAt=dict.get("updatedAt"),
        )
        return listing_dto

    def dto_2_dict(self, dto: ListingDTO) -> dict:
        return dto.__dict__


class ListingMapper(RepositoryMapper):

    def get_type(self) -> type:
        return GenericListing.__class__

    def entity_2_dto(self, entity: GenericListing) -> ListingDTO:
        property_dtos = []
        for property in entity.properties:
            property_dto = PropertyDTO(
                id=property.id,
                width=property.width,
                length=property.length,
            )
            property_dtos.append(property_dto)

        sale_dto = ListingDTO(
            id=entity.id,
            properties=property_dtos,
            createdAt=entity.created_at.strftime("%d/%m/%Y %I:%M %p"),
            updatedAt=entity.updated_at.strftime("%d/%m/%Y %I:%M %p"),
        )
        return sale_dto

    def dto_2_entity(self, dto: ListingDTO) -> GenericListing:
        listing = GenericListing()
        listing.id = UUID(dto.id)

        properties = []
        for property_dto in dto.properties:
            property = Property(
                id=property_dto.id,
                width=property_dto.width,
                length=property_dto.length,
            )
            properties.append(property)

        listing.properties = properties
        return listing
