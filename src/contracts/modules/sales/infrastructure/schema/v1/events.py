from pulsar.schema import Record, String, Float, Integer

from contracts.seedwork.infrastructure.schema.v1.events import IntegrationEvent


class SaleRegisteredPayload(Record):
    sale_id = String()
    property_id = String()
    price = Float()
    currency = String()
    executed_at = Integer()


class SaleRegisteredEvent(IntegrationEvent):
    data = SaleRegisteredPayload()
