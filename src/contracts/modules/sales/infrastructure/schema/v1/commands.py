from pulsar.schema import String, Float

from contracts.seedwork.infrastructure.schema.v1.commands import IntegrationCommand


class RegisterSaleCommandPayload(IntegrationCommand):
    propertyId = String()
    price = Float()
    currency = String()
    executedAt = String()


class RegisterSaleCommand(IntegrationCommand):
    data = RegisterSaleCommandPayload()


class DeleteSaleCommandPayload(IntegrationCommand):
    saleId = String()


class DeleteSaleCommand(IntegrationCommand):
    data = DeleteSaleCommandPayload()
