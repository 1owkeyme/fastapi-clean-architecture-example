from domain import entities

from . import interfaces


class GetAllMoviesUsecase:
    def __init__(self, movie_repository: interfaces.MovieRepository) -> None:
        self._movie_repository = movie_repository

    async def execute(self) -> list[entities.movie.Movie]:
        return await self._movie_repository.get_all_movies()
