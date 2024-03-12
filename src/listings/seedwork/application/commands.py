from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import singledispatch


class Command: ...


@dataclass
class CommandResult:
    data: any


class CommandHandler(ABC):

    @abstractmethod
    def handle(self, command: Command) -> CommandResult:
        raise NotImplementedError()


@singledispatch
def execute_command(command: Command):
    name = type(command).__name__
    raise NotImplementedError(f"No implementation found for command {name}")
