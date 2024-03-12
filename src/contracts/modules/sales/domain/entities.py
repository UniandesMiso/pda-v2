from datetime import datetime
from dataclasses import dataclass, field

from contracts.seedwork.domain.entities import Contract
from contracts.seedwork.domain.mixins import ValidateRules
from contracts.modules.sales.domain.events import SaleRegistered


@dataclass
class Sale(Contract, ValidateRules):
    executed_at: datetime = field(default=datetime.now())

    def register_sale(self):
        event = SaleRegistered(
            sale_id=str(self.id),
            property_id=self.property_id,
            price=self.amount.price,
            currency=self.amount.currency,
            executed_at=self.executed_at,
        )
        self.add_event(event)
