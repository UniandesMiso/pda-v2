from pydispatch import dispatcher

from contracts.modules.sales.application.handlers import SalesHandler
from contracts.modules.sales.domain.events import SaleRegistered


dispatcher.connect(SalesHandler.handle_sale_registered, signal=SaleRegistered.__name__)
