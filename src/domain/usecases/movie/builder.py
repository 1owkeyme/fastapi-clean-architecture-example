from . import interfaces
from .create import CreateMovieUsecase
from .delete import DeleteMovieUsecase


class MovieUsecasesBuilder:
    def __init__(self, movie_repository: interfaces.MovieRepository) -> None:
        self._movie_repository = movie_repository

    def construct_create_movie_usecase(self) -> CreateMovieUsecase:
        return CreateMovieUsecase(movie_repository=self._movie_repository)

    def construct_delete_movie_usecase(self) -> DeleteMovieUsecase:
        return DeleteMovieUsecase(movie_repository=self._movie_repository)
