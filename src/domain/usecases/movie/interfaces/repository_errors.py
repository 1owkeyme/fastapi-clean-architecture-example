class MovieRepositoryError(Exception):
    pass


class MovieAlreadyExistsError(MovieRepositoryError):
    pass


class MovieNotFoundError(MovieRepositoryError):
    pass
