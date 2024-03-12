from dataclasses import dataclass

from contracts.seedwork.domain.events import DomainEvent
from contracts.seedwork.domain.factories import Factory
from contracts.seedwork.domain.exceptions import FactoryException
from contracts.seedwork.infrastructure.schema.v1.events import IntegrationEvent
from contracts.modules.sales.domain.events import SaleRegistered
from contracts.modules.sales.infrastructure.schema.v1.events import SaleRegisteredPayload, SaleRegisteredEvent


@dataclass
class FactoryEvents(Factory):

    def create_object(self, event: DomainEvent) -> IntegrationEvent:
        if event.get_type() == SaleRegistered.__class__:
            payload = SaleRegisteredPayload(
                sale_id=str(event.id),
                property_id=event.property_id,
                price=event.price,
                currency=event.currency,
                executed_at=int(event.executed_at.timestamp()),
            )
            return SaleRegisteredEvent(data=payload)

        else:
            raise FactoryException("The factory does not exist for the requested type")
