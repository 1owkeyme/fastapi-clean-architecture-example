from domain import entities

from ..error_handlers import handle_usecases_errors
from . import interfaces


class GetAllMovieReviewsUsecase:
    def __init__(self, movie_repository: interfaces.MovieRepository) -> None:
        self._movie_repository = movie_repository

    @handle_usecases_errors
    async def execute(self, movie_id: entities.movie.MovieId) -> list[entities.review.ReviewForMovie]:
        return await self._movie_repository.get_all_movie_reviews(id_entity=movie_id)
