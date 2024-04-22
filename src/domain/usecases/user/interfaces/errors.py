class UserUsecaseError(Exception):
    pass


class InvalidCredentialsError(UserUsecaseError):
    pass
