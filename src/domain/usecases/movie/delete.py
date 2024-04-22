from domain import entities

from . import interfaces


class DeleteMovieUsecase:
    def __init__(self, movie_repository: interfaces.MovieRepository) -> None:
        self._movie_repository = movie_repository

    async def execute(self, movie_id: entities.movie.MovieId) -> entities.movie.MovieId:
        return await self._movie_repository.delete_movie(id_entity=movie_id)
