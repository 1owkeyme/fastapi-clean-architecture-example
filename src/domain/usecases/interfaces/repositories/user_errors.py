class UserRepositoryCriticalError(Exception):
    pass


class UserRepositoryError(Exception):
    pass


class UserAlreadyExistsError(UserRepositoryError):
    pass


class UserNotFoundError(UserRepositoryError):
    pass
