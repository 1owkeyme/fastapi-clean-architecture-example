from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors
from . import errors as err


class GetMovieByIdUsecase:
    def __init__(self, movie_repository: interfaces.repositories.MovieRepository) -> None:
        self._movie_repository = movie_repository

    @handle_usecases_errors
    async def execute(self, movie_id: entities.Id) -> entities.movie.Movie:
        try:
            return await self._movie_repository.get_movie_by_id(id_entity=movie_id)
        except interfaces.repositories.movie_errors.MovieNotFoundError:
            raise err.MovieNotFoundError from None
