from domain import entities

from . import interfaces


class GetMovieByIdUsecase:
    def __init__(self, movie_repository: interfaces.MovieRepository) -> None:
        self._movie_repository = movie_repository

    async def execute(self, movie_id: entities.movie.MovieId) -> entities.movie.Movie:
        return await self._movie_repository.get_movie_by_id(id_entity=movie_id)
