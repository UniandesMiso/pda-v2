from dataclasses import dataclass

from listings.seedwork.domain.events import DomainEvent
from listings.seedwork.domain.factories import Factory
from listings.seedwork.domain.exceptions import FactoryException
from listings.seedwork.infrastructure.schema.v1.events import IntegrationEvent
from listings.modules.information.domain.events import PropertyProcessed
from listings.modules.information.infrastructure.schema.v1.events import PropertyProcessedPayload, PropertyProcessedEvent


@dataclass
class FactoryEvents(Factory):

    def create_object(self, event: DomainEvent) -> IntegrationEvent:
        if event.get_type() == PropertyProcessed.__class__:
            payload = PropertyProcessedPayload(
                property_id=event.property_id,
                width=event.width,
                length=event.length
            )
            return PropertyProcessedEvent(data=payload)

        else:
            raise FactoryException("The factory does not exist for the requested type")
