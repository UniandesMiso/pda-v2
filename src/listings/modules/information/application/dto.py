from dataclasses import dataclass, field

from listings.seedwork.application.dto import DTO


@dataclass(frozen=True)
class PropertyDTO(DTO):
    id: str = field(default_factory=str)
    width: float = field(default_factory=float)
    length: float = field(default_factory=float)


@dataclass(frozen=True)
class ListingDTO(DTO):
    id: str = field(default_factory=str)
    properties: list[PropertyDTO] = field(default_factory=list)
    createdAt: str = field(default_factory=str)
    updatedAt: str = field(default_factory=str)
