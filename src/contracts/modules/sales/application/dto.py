from dataclasses import dataclass, field

from contracts.seedwork.application.dto import DTO


@dataclass(frozen=True)
class SaleDTO(DTO):
    id: str = field(default_factory=str)
    propertyId: str = field(default_factory=str)
    createdAt: str = field(default_factory=str)
    updatedAt: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    executedAt: str = field(default_factory=str)
