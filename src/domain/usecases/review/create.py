from domain import entities

from . import interfaces


class CreateReviewUsecase:
    def __init__(self, review_repository: interfaces.ReviewRepository) -> None:
        self._review_repository = review_repository

    async def execute(self, review_info: entities.review.ReviewInfo) -> None:
        await self._review_repository.create_review(info=review_info)
