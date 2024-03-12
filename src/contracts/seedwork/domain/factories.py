from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create_object(obj: type) -> any: ...
