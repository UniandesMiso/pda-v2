from pulsar import Client
from pulsar.schema import AvroSchema

from listings.seedwork.infrastructure.utils import get_pulsar_url
from listings.modules.information.infrastructure.factories import FactoryEvents


class Dispatcher:

    def __init__(self):
        self.factory = FactoryEvents()

    def _send_message(self, topic, message, schema):
        client = Client(get_pulsar_url())
        producer = client.create_producer(topic, schema=schema)
        producer.send(message)
        client.close()

    def send_event(self, topic, event):
        message = self.factory.create_object(event)
        self._send_message(topic, message, AvroSchema(type(message)))
