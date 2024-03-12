from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field

from contracts.seedwork.domain.events import DomainEvent


@dataclass
class SaleRegistered(DomainEvent):

    def get_type(self):
        return SaleRegistered.__class__

    sale_id: str = field(default_factory=str)
    property_id: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    executed_at: datetime = field(default_factory=datetime)


@dataclass
class SaleRegisterFailed(DomainEvent):

    def get_type(self):
        return SaleRegisterFailed.__class__

    sale_id: str = field(default_factory=str)
    property_id: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    executed_at: datetime = field(default_factory=datetime)
