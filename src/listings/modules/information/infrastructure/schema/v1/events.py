from pulsar.schema import Record, String, Float, Integer

from listings.seedwork.infrastructure.schema.v1.events import IntegrationEvent


class PropertyProcessedPayload(Record):
    property_id = String()
    width = Float()
    length = Float()


class PropertyProcessedEvent(IntegrationEvent):
    data = PropertyProcessedPayload()
