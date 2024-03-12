from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class DTO: ...


class Mapper(ABC):

    @abstractmethod
    def dict_2_dto(self, dict: dict) -> DTO: ...

    @abstractmethod
    def dto_2_dict(self, dto: DTO) -> dict: ...
