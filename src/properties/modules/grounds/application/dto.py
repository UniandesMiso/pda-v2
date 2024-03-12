from dataclasses import dataclass, field

from properties.seedwork.application.dto import DTO


@dataclass(frozen=True)
class GroundDTO(DTO):
    id: str = field(default_factory=str)
    createdAt: str = field(default_factory=str)
    updatedAt: str = field(default_factory=str)
    address: str = field(default_factory=str)
    width: float = field(default_factory=float)
    length: float = field(default_factory=float)
    location: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
