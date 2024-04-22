from domain import entities

from . import interfaces


class GetReviewByIdUsecase:
    def __init__(self, review_repository: interfaces.ReviewRepository) -> None:
        self._review_repository = review_repository

    async def execute(self, review_id: entities.review.ReviewId) -> None:
        await self._review_repository.delete_review(id_entity=review_id)
