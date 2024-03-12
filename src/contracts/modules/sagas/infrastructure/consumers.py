from logging import error
from pulsar import Client
from pulsar.schema import AvroSchema

from contracts.seedwork.infrastructure.utils import get_pulsar_url
from contracts.modules.sagas.application.coordinators.sales_saga import listen_event
from contracts.modules.sagas.domain.events.grounds import AmountUpdated, AmountUpdateFailed
from contracts.modules.sagas.infrastructure.schema.v1.events import AmountUpdatedEvent, AmountUpdateFailedEvent


def subscribe_2_ground_events(app):
    client = Client(get_pulsar_url())

    consumer = client.subscribe(
        topic="grounds-events",
        subscription_name="grounds-events-sagas-sub",
        schema=AvroSchema(AmountUpdatedEvent),
    )

    while True:
        message = consumer.receive()
        try:
            event = message.value()
            with app.app_context():
                inner_event = AmountUpdated(
                    property_id=event.data.property_id,
                    sale_id=event.data.sale_id,
                    price=event.data.price,
                    currency=event.data.currency,
                )
                listen_event(inner_event)
            consumer.acknowledge(message)
        except Exception as ex:
            error(str(ex))
            consumer.negative_acknowledge(message)


def subscribe_2_ground_errors_events(app):
    client = Client(get_pulsar_url())

    consumer = client.subscribe(
        topic="grounds-events-errors",
        subscription_name="grounds-events-errors-sagas-sub",
        schema=AvroSchema(AmountUpdateFailedEvent),
    )

    while True:
        message = consumer.receive()
        try:
            event = message.value()
            with app.app_context():
                inner_event = AmountUpdateFailed(
                    property_id=event.data.property_id,
                    sale_id=event.data.sale_id,
                    price=event.data.price,
                    currency=event.data.currency,
                )
                listen_event(inner_event)
            consumer.acknowledge(message)
        except Exception as ex:
            error(str(ex))
            consumer.negative_acknowledge(message)
