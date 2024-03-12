from dataclasses import dataclass, field


@dataclass(frozen=True)
class ValueObject: ...


@dataclass(frozen=True)
class Amount(ValueObject):
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
