from .. import errors as base_err


class UserUsecaseError(base_err.UsecaseError):
    pass


class UserNotFoundError(UserUsecaseError):
    pass


class UserAlreadyExistsError(UserUsecaseError):
    pass


class FirstSuperUserDeleteForbiddenError(UserUsecaseError):
    pass
