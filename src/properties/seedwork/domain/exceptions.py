from werkzeug.exceptions import HTTPException


class DomainException(HTTPException): ...


class FactoryException(DomainException):

    def __init__(self, message: str):
        self.code = 500
        self.description = message
