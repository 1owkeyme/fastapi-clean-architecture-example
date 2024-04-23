class AuthError(Exception):
    pass


class UnauthenticatedError(AuthError):
    pass


class UnauthorizedError(AuthError):
    pass
