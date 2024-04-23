from .. import errors as base_err


class MovieRepositoryCriticalError(base_err.UsecaseCriticalError):
    pass


class MovieRepositoryError(base_err.UsecaseError):
    pass


class MovieAlreadyExistsError(MovieRepositoryError):
    pass


class MovieNotFoundError(MovieRepositoryError):
    pass
