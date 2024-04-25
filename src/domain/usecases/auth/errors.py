from .. import errors as base_err


class AuthUsecaseError(base_err.UsecaseError):
    pass


class InvalidCredentialsError(AuthUsecaseError):
    pass
