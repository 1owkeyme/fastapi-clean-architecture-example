from .. import errors as base_err


class UserRepositoryCriticalError(base_err.UsecaseCriticalError):
    pass


class UserRepositoryError(base_err.UsecaseError):
    pass


class UserAlreadyExistsError(UserRepositoryError):
    pass


class UserNotFoundError(UserRepositoryError):
    pass
