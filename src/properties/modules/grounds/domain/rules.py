from contracts.seedwork.domain.rules import BusinessRule
from contracts.modules.sales.domain.entities import Sale


class PriceRequired(BusinessRule):

    _message = "The price is required"

    def __init__(self, sale: Sale):
        super().__init__(self._message)
        self.sale = sale

    def is_valid(self) -> bool:
        return self.sale.amount is not None
