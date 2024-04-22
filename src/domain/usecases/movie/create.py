from domain import entities

from . import interfaces


class CreateMovieUsecase:
    def __init__(self, movie_repository: interfaces.MovieRepository) -> None:
        self._movie_repository = movie_repository

    async def execute(self, movie_info: entities.movie.MovieInfo) -> entities.movie.MovieId:
        return await self._movie_repository.create_movie(info_entity=movie_info)
