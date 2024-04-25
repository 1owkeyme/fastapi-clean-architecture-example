from .. import errors as base_err


class MovieUsecaseError(base_err.UsecaseError):
    pass


class MovieNotFoundError(MovieUsecaseError):
    pass


class MovieAlreadyExistsError(MovieUsecaseError):
    pass
