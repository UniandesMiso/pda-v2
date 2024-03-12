from abc import ABC

from contracts.seedwork.domain.repositories import Repository


class SaleRepository(Repository, ABC): ...
