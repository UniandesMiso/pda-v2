from listings.seedwork.application.handlers import Handler

from listings.modules.information.infrastructure.dispatchers import Dispatcher


class InformationHandler(Handler):

    @staticmethod
    def handle_property_processed(event):
        dispatcher = Dispatcher()
        dispatcher.send_event("listing-information-events", event)
