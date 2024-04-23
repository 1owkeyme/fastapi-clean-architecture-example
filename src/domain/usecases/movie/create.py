from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors


class CreateMovieUsecase:
    def __init__(self, movie_repository: interfaces.repositories.MovieRepository) -> None:
        self._movie_repository = movie_repository

    @handle_usecases_errors
    async def execute(self, movie_info: entities.movie.MovieInfo) -> entities.Id:
        return await self._movie_repository.create_movie(info_entity=movie_info)
