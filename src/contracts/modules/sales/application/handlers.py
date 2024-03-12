from contracts.seedwork.application.handlers import Handler

from contracts.modules.sagas.application.coordinators.sales_saga import listen_event


class SalesHandler(Handler):

    @staticmethod
    def handle_sale_registered(event):
        listen_event(event)
