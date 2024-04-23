from domain import entities

from .. import interfaces


class GetReviewByIdUsecase:
    def __init__(self, review_repository: interfaces.repositories.ReviewRepository) -> None:
        self._review_repository = review_repository

    async def execute(self, review_id: entities.Id) -> entities.review.Review:
        return await self._review_repository.get_review_by_id(id_entity=review_id)
