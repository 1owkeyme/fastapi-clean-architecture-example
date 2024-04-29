from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors
from ..movie import GetMovieByIdUsecase
from . import errors as err


class CreateReviewByMovieIdUsecase:
    def __init__(self, review_repository: interfaces.repositories.ReviewRepository) -> None:
        self._review_repository = review_repository

    @handle_usecases_errors
    async def execute(
        self,
        user_id: entities.Id,
        movie_id: entities.Id,
        get_movie_by_id_usecase: GetMovieByIdUsecase,
        review_info: entities.review.ReviewInfo,
    ) -> entities.Id:
        existing_movie = await get_movie_by_id_usecase.execute(movie_id)
        try:
            return await self._review_repository.create_review_by_movie_id(
                user_id_entity=user_id,
                movie_id_entity=existing_movie,
                info_entity=review_info,
            )
        except interfaces.repositories.review_errors.ReviewAlreadyExistsError:
            raise err.ReviewAlreadyExistsError from None
