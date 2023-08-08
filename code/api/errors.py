AUTH_ERROR = "authorization error"
CONNECTION_ERROR = "connection error"
INVALID_ARGUMENT = "invalid argument"
UNKNOWN = "unknown"
NOT_FOUND = 'not found'
INTERNAL = 'internal error'
HEALTH_CHECK_ERROR = 'health check failed'


class CTRBaseError(Exception):
    def __init__(self, code, message, type_='fatal'):
        super().__init__()
        self.code = code or UNKNOWN
        self.message = message or 'Something went wrong.'
        self.type_ = type_

    @property
    def json(self):
        return {'type': self.type_,
                'code': self.code.lower(),
                'message': self.message}


class BadRequestError(CTRBaseError):
    def __init__(self, message):
        super().__init__(
            INVALID_ARGUMENT,
            f'Invalid JSON payload received. {message}'
        )

class AuthorizationError(CTRBaseError):
    def __init__(self, message):
        super().__init__(AUTH_ERROR, f"Authorization failed: {message}")


class InvalidArgumentError(CTRBaseError):
    def __init__(self, message):
        super().__init__(INVALID_ARGUMENT, str(message))

