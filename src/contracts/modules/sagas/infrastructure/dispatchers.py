from pulsar import Client

from contracts.modules.sagas.infrastructure.utils import get_pulsar_url, get_json_schema, get_avro_schema


class Dispatcher:

    def send_message(self, message, topic):
        json_schema = get_json_schema(topic)
        avro_schema = get_avro_schema(json_schema)

        client = Client(get_pulsar_url())
        producer = client.create_producer(topic, schema=avro_schema)
        producer.send(message)
        client.close()
