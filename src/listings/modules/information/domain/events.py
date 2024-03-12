from uuid import UUID
from dataclasses import dataclass, field

from listings.seedwork.domain.events import DomainEvent


@dataclass
class PropertyProcessed(DomainEvent):

    def get_type(self):
        return PropertyProcessed.__class__

    property_id: str = field(default_factory=UUID)
    width: float = field(default_factory=float)
    length: float = field(default_factory=float)
