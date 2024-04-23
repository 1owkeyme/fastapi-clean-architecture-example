from domain import entities

from .. import interfaces


class CreateReviewUsecase:
    def __init__(self, review_repository: interfaces.repositories.ReviewRepository) -> None:
        self._review_repository = review_repository

    async def execute(
        self,
        user_id: entities.Id,
        movie_id: entities.Id,
        review_info: entities.review.ReviewInfo,
    ) -> entities.Id:
        return await self._review_repository.create_review_by_movie_id(
            user_id_entity=user_id,
            movie_id_entity=movie_id,
            info_entity=review_info,
        )
