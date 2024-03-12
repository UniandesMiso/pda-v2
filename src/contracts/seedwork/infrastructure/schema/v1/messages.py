from uuid import uuid4
from pulsar.schema import Record, String, Long

from contracts.seedwork.infrastructure.utils import time_millis


class Message(Record):
    id = String(default=str(uuid4()))
    ingestion = Long(default=time_millis())
