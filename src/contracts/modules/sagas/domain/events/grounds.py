from dataclasses import dataclass

from contracts.seedwork.domain.events import DomainEvent


class GroundEvent(DomainEvent): ...


@dataclass
class AmountUpdated(GroundEvent):

    def get_type(self):
        return AmountUpdated.__class__

    property_id: str = None
    sale_id: str = None
    price: float = None
    currency: str = None


@dataclass
class AmountUpdateFailed(GroundEvent):

    def get_type(self):
        return AmountUpdateFailed.__class__
    
    property_id: str = None
    sale_id: str = None
    price: float = None
    currency: str = None
