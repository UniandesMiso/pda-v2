from pulsar.schema import Record, String, Float

from contracts.seedwork.infrastructure.schema.v1.events import IntegrationEvent


class AmountUpdatedPayload(Record):
    property_id = String()
    sale_id = String()
    price = Float()
    currency = String()


class AmountUpdatedEvent(IntegrationEvent):
    data = AmountUpdatedPayload()


class AmountUpdateFailedPayload(Record):
    property_id = String()
    sale_id = String()
    price = Float()
    currency = String()


class AmountUpdateFailedEvent(IntegrationEvent):
    data = AmountUpdateFailedPayload()
