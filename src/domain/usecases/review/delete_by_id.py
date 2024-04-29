from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors
from . import errors as err


class DeleteReviewByIdUsecase:
    def __init__(self, review_repository: interfaces.repositories.ReviewRepository) -> None:
        self._review_repository = review_repository

    @handle_usecases_errors
    async def execute(self, review_id: entities.Id) -> entities.Id:
        try:
            return await self._review_repository.delete_review_by_id(id_entity=review_id)
        except interfaces.repositories.review_errors.ReviewNotFoundError:
            raise err.ReviewNotFoundError from None
