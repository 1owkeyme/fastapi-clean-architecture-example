from domain import entities

from . import interfaces


class DeleteMovieUsecase:
    def __init__(self, movie_repository: interfaces.MovieRepository) -> None:
        self._movie_repository = movie_repository

    async def execute(self, movie_id: entities.movie.MovieId) -> None:
        await self._movie_repository.delete_movie(id_=movie_id)
