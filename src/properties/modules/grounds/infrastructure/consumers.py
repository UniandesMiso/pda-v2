from logging import error
from pulsar import Client
from pulsar.schema import AvroSchema

from properties.seedwork.application.commands import execute_command
from properties.seedwork.infrastructure.utils import get_pulsar_url
from properties.modules.grounds.application.commands.register_ground import RegisterGround
from properties.modules.grounds.application.commands.update_amount import UpdateAmount
from properties.modules.grounds.infrastructure.schema.v1.commands import RegisterGroundCommand, UpdateAmountCommand


def subscribe_2_register_ground_command(app):
    client = Client(get_pulsar_url())

    consumer = client.subscribe(
        topic="register-ground-command",
        subscription_name="register-ground-command-sub",
        schema=AvroSchema(RegisterGroundCommand),
    )

    while True:
        message = consumer.receive()
        try:
            command = message.value()
            with app.app_context():
                command = RegisterGround(
                    address=command.data.address,
                    location=command.data.location,
                )
                execute_command(command)
            consumer.acknowledge(message)
        except Exception as ex:
            error(str(ex))
            consumer.negative_acknowledge(message)


def subscribe_2_update_amount_command(app):
    client = Client(get_pulsar_url())

    consumer = client.subscribe(
        topic="update-amount-command",
        subscription_name="update-amount-command-sub",
        schema=AvroSchema(UpdateAmountCommand),
    )

    while True:
        message = consumer.receive()
        try:
            command = message.value()
            with app.app_context():
                command = UpdateAmount(
                    property_id=command.data.propertyId,
                    sale_id=command.data.saleId,
                    price=command.data.price,
                    currency=command.data.currency,
                )
                execute_command(command)
            consumer.acknowledge(message)
        except Exception as ex:
            error(str(ex))
            consumer.negative_acknowledge(message)
