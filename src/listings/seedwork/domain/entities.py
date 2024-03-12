from uuid import UUID, uuid4
from datetime import datetime
from dataclasses import dataclass, field

from listings.seedwork.domain.events import DomainEvent
from listings.seedwork.domain.value_objects import Property


@dataclass
class Entity:
    id: UUID = field(hash=True, default=uuid4())
    created_at: datetime = field(default=datetime.now())
    updated_at: datetime = field(default=datetime.now())


@dataclass
class Root(Entity):
    events: list[DomainEvent] = field(default_factory=list)

    def add_event(self, event):
        self.events.append(event)

    def clear_events(self):
        self.events = list()


@dataclass
class Listing(Root):
    properties: list[Property] = field(default_factory=list[Property])
