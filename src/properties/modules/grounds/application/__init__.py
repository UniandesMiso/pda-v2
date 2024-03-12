from pydispatch import dispatcher

from properties.modules.grounds.application.handlers import GroundsHandler
from properties.modules.grounds.domain.events import AmountUpdated, AmountUpdateFailed


dispatcher.connect(GroundsHandler.handle_amount_updated, signal=AmountUpdated.__name__)
dispatcher.connect(GroundsHandler.handle_amount_update_failed, signal=AmountUpdateFailed.__name__)
