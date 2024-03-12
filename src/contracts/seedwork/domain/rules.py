from abc import ABC, abstractmethod


class BusinessRule(ABC):

    _message = "Invalid business rule"

    def __init__(self, message):
        self._message = message

    def error(self):
        return self._message

    @abstractmethod
    def is_valid(self) -> bool: ...
