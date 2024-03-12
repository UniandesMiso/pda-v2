from werkzeug.exceptions import HTTPException

from listings.seedwork.domain.rules import BusinessRule


class DomainException(HTTPException): ...


class BusinessRuleException(DomainException):

    def __init__(self, rule: BusinessRule):
        self.code = 400
        self.description = rule.error()


class FactoryException(DomainException):

    def __init__(self, message: str):
        self.code = 500
        self.description = message
