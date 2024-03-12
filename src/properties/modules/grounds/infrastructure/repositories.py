from uuid import UUID
from datetime import datetime

from properties.config.db import db
from properties.modules.grounds.domain.entities import Ground
from properties.modules.grounds.domain.repositories import GroundRepository
from properties.modules.grounds.infrastructure.mappers import GroundMapper
from properties.modules.grounds.infrastructure.dto import Ground as GroundDTO


class GroundRepositorySQL(GroundRepository):

    def create(self, entity: Ground):
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        mapper = GroundMapper()
        ground_dto = mapper.entity_2_dto(entity)
        db.session.add(ground_dto)
        db.session.commit()

    def update(self, entity: Ground):
        values = {"updated_at": datetime.now()}
        if (entity.dimension.width): values.update(width=entity.dimension.width)
        if (entity.dimension.length): values.update(length=entity.dimension.length)
        if (entity.amount.price): values.update(price=entity.amount.price)
        if (entity.amount.currency): values.update(currency=entity.amount.currency)
        db.session.query(GroundDTO).filter(GroundDTO.id == str(entity.id)).update(values)
        db.session.commit()

    def get_by_id(self, id: UUID) -> Ground:
        ground_dto = db.session.query(GroundDTO).get(id)
        mapper = GroundMapper()
        ground = mapper.dto_2_entity(ground_dto)
        return ground
