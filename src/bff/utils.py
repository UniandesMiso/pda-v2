from os import environ
from time import time
from json import loads
from requests import get
from pulsar.schema import AvroSchema
from fastavro.schema import parse_schema


def get_pulsar_url():
    host = environ.get("BROKER_HOST", "localhost")
    port = environ.get("BROKER_PORT", "6650")
    return f"pulsar://{host}:{port}"


def get_json_schema(topic):
    host = environ.get("BROKER_HOST", "localhost")
    name = f"public/default/{topic}"
    response = get(f"http://{host}:8080/admin/v2/schemas/{name}/schema")
    return loads(response.json().get("data", {}))


def get_avro_schema(json_schema):
    schema = parse_schema(json_schema)
    return AvroSchema(None, schema_definition=schema)


def get_properties_url():
    return (
        "http://"
        + f"{environ.get('PROPERTIES_HOST', 'localhost')}:"
        + f"{environ.get('PROPERTIES_PORT', '3000')}"
    )


def get_listings_url():
    return (
        "http://"
        + f"{environ.get('LISTINGS_HOST', 'localhost')}:"
        + f"{environ.get('LISTINGS_PORT', '3002')}"
    )


def time_millis():
    return int(time() * 1000)
