from dataclasses import dataclass, field


@dataclass(frozen=True)
class ValueObject: ...


@dataclass(frozen=True)
class Property(ValueObject):
    id: str = field(default_factory=str)
    width: float = field(default_factory=float)
    length: float = field(default_factory=float)
