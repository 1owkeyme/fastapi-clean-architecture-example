class ReviewRepositoryCriticalError(Exception):
    pass


class ReviewRepositoryError(Exception):
    pass


class ReviewAlreadyExistsError(ReviewRepositoryError):
    pass


class ReviewNotFoundError(ReviewRepositoryError):
    pass
