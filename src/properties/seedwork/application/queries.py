from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import singledispatch


class Query: ...


@dataclass
class QueryResult:
    data: None


class QueryHandler(ABC):

    @abstractmethod
    def handle(self, query: Query) -> QueryResult:
        raise NotImplementedError()


@singledispatch
def execute_query(query: Query):
    name = type(query).__name__
    raise NotImplementedError(f"No implementation found for query {name}")
