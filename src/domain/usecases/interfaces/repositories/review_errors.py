from .. import errors as base_err


class ReviewRepositoryCriticalError(base_err.UsecaseCriticalError):
    pass


class ReviewRepositoryError(base_err.UsecaseError):
    pass


class ReviewAlreadyExistsError(ReviewRepositoryError):
    pass


class ReviewNotFoundError(ReviewRepositoryError):
    pass
