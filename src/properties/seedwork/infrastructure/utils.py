from os import environ
from time import time


def time_millis():
    return int(time() * 1000)


def get_pulsar_url():
    host = environ.get("BROKER_HOST", "localhost")
    port = environ.get("BROKER_PORT", "6650")
    return f"pulsar://{host}:{port}"
