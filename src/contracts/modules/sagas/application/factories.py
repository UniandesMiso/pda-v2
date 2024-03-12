from dataclasses import dataclass

from contracts.seedwork.application.commands import Command
from contracts.seedwork.domain.events import DomainEvent
from contracts.seedwork.domain.factories import Factory
from contracts.seedwork.domain.exceptions import FactoryException
from contracts.modules.sales.application.commands.delete_sale import DeleteSale
from contracts.modules.sales.domain.events import SaleRegistered
from contracts.modules.sagas.application.commands.grounds import UpdateAmount
from contracts.modules.sagas.domain.events.grounds import AmountUpdateFailed


@dataclass
class FactoryCommands(Factory):

    def create_object(self, event: DomainEvent) -> Command:
        if type(event).__name__ == SaleRegistered.__name__:
            return UpdateAmount(
                property_id=event.property_id,
                sale_id=event.sale_id,
                price=event.price,
                currency=event.currency
            )

        if type(event).__name__ == AmountUpdateFailed.__name__:
            return DeleteSale(id=event.sale_id)

        else:
            raise FactoryException("The factory does not exist for the requested type")
