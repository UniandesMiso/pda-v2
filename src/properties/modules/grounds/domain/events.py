from dataclasses import dataclass, field

from properties.seedwork.domain.events import DomainEvent


@dataclass
class AmountUpdated(DomainEvent):

    def get_type(self):
        return AmountUpdated.__class__

    property_id: str = field(default_factory=str)
    sale_id: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)


@dataclass
class AmountUpdateFailed(DomainEvent):

    def get_type(self):
        return AmountUpdateFailed.__class__

    property_id: str = field(default_factory=str)
    sale_id: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
