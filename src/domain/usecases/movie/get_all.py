from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors


class GetAllMoviesUsecase:
    def __init__(self, movie_repository: interfaces.repositories.MovieRepository) -> None:
        self._movie_repository = movie_repository

    @handle_usecases_errors
    async def execute(self) -> list[entities.movie.Movie]:
        return await self._movie_repository.get_all_movies()
