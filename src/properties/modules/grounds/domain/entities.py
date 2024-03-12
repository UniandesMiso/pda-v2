from dataclasses import dataclass

from properties.seedwork.domain.entities import Property
from properties.modules.grounds.domain.events import AmountUpdated


@dataclass
class Ground(Property):

    def update_amount(self, sale_id):
        event = AmountUpdated(
            property_id=self.id,
            sale_id=sale_id,
            price=self.amount.price,
            currency=self.amount.currency,
        )
        self.add_event(event)
