from pulsar.schema import String, Float

from properties.seedwork.infrastructure.schema.v1.commands import IntegrationCommand


class RegisterGroundPayload(IntegrationCommand):
    address = String()
    location = String()


class RegisterGroundCommand(IntegrationCommand):
    data = RegisterGroundPayload()


class UpdateAmountPayload(IntegrationCommand):
    propertyId = String()
    saleId = String()
    price = Float()
    currency = String()


class UpdateAmountCommand(IntegrationCommand):
    data = UpdateAmountPayload()
