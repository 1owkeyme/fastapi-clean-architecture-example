from .. import errors as base_err


class ReviewUsecaseError(base_err.UsecaseError):
    pass


class ReviewNotFoundError(ReviewUsecaseError):
    pass


class ReviewAlreadyExistsError(ReviewUsecaseError):
    pass
