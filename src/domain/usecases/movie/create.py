from domain import entities

from . import interfaces


class CreateMovieUsecase:
    def __init__(self, movie_repository: interfaces.MovieRepository) -> None:
        self._movie_repository = movie_repository

    async def execute(self, movie_info: entities.movie.MovieInfo) -> None:
        await self._movie_repository.create_movie(info=movie_info)
