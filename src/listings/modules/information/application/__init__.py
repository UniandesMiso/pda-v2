from pydispatch import dispatcher

from listings.modules.information.application.handlers import InformationHandler
from listings.modules.information.domain.events import PropertyProcessed


dispatcher.connect(InformationHandler.handle_property_processed, signal=PropertyProcessed.__name__)
