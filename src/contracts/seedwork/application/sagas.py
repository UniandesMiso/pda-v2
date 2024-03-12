from uuid import UUID
from datetime import datetime
from copy import deepcopy
from abc import ABC, abstractmethod
from dataclasses import dataclass

from contracts.seedwork.application.commands import Command, execute_command
from contracts.seedwork.domain.events import DomainEvent


class Coordinator(ABC):
    id: UUID

    @abstractmethod
    def start(self): ...

    @abstractmethod
    def finish(self): ...

    @abstractmethod
    def initialize_steps(self): ...

    @abstractmethod
    def save_log(self, step): ...

    @abstractmethod
    def process_event(self, event: DomainEvent): ...

    @abstractmethod
    def build_command(self, event: DomainEvent, command_type: type) -> Command: ...

    def send_command(self, event: DomainEvent, command_type: type):
        command = self.build_command(event, command_type)
        execute_command(command)


class Step():
    id: UUID
    index: int
    executed_at: datetime


@dataclass
class Start(Step): 
    index: int = 0


@dataclass
class End(Step):
    index: int = 0


@dataclass
class Transaction(Step):
    index: int
    command: Command
    event: DomainEvent
    error: DomainEvent
    compensation: Command


class OrchestrationCoordinator(Coordinator):
    index: int
    steps: list[Step]

    def is_first(self, index):
        return index == 1

    def is_last(self, index):
        return len(self.steps) - 2 == index
    
    def has_to_finish(self, event, i, step):
        return (
            (self.is_first(i) and isinstance(event, step.error)) or
            (self.is_last(i) and not isinstance(event, step.error))
        )

    def get_step_by_event(self, event: DomainEvent):
        for i, step in enumerate(self.steps):
            if not isinstance(step, Transaction): continue
            if isinstance(event, step.event): return i, step
            if isinstance(event, step.error): return i, step
        return None
    
    def process_event(self, event: DomainEvent):
        i, step = self.get_step_by_event(event)
        if self.is_first(i):
            self.start()
        if self.has_to_finish(event, i, step):
            self.finish()
        elif isinstance(event, step.error):
            self.send_command(event, self.steps[i - 1].compensation)
            copy = deepcopy(step)
            copy.event = copy.error
            copy.command = self.steps[i - 1].compensation
            self.save_log(copy)
            if self.is_last(i): self.finish()
        elif isinstance(event, step.event):
            self.send_command(event, self.steps[i + 1].command)
            copy = deepcopy(step)
            copy.event = copy.event
            copy.command = self.steps[i + 1].command
            self.save_log(copy)
