from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors
from . import errors as err


class GetAllMovieReviewsByIdUsecase:
    def __init__(self, movie_repository: interfaces.repositories.MovieRepository) -> None:
        self._movie_repository = movie_repository

    @handle_usecases_errors
    async def execute(self, movie_id: entities.Id) -> list[entities.review.ReviewForMovie]:
        try:
            return await self._movie_repository.get_all_movie_reviews_by_id(id_entity=movie_id)
        except interfaces.repositories.movie_errors.MovieNotFoundError:
            raise err.MovieNotFoundError from None
