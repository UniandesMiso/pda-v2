from logging import error
from pulsar import Client
from pulsar.schema import AvroSchema

from contracts.seedwork.application.commands import execute_command
from contracts.seedwork.infrastructure.utils import get_pulsar_url
from contracts.modules.sales.application.commands.register_sale import RegisterSale
from contracts.modules.sales.infrastructure.schema.v1.commands import RegisterSaleCommand


def subscribe_2_register_sale_command(app):
    client = Client(get_pulsar_url())

    consumer = client.subscribe(
        topic="register-sale-command",
        subscription_name="register-sale-command-sub",
        schema=AvroSchema(RegisterSaleCommand),
    )

    while True:
        message = consumer.receive()
        try:
            command = message.value()
            with app.app_context():
                command = RegisterSale(
                    property_id=command.data.propertyId,
                    price=command.data.price,
                    currency=command.data.currency,
                    executed_at=command.data.executedAt,
                )
                execute_command(command)
            consumer.acknowledge(message)
        except Exception as ex:
            error(str(ex))
            consumer.negative_acknowledge(message)
