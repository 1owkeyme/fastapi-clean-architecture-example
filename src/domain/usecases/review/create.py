from domain import entities

from . import interfaces


class CreateReviewUsecase:
    def __init__(self, review_repository: interfaces.ReviewRepository) -> None:
        self._review_repository = review_repository

    async def execute(
        self,
        user_id: entities.user.UserId,
        movie_id: entities.movie.MovieId,
        review_contents: entities.review.ReviewContents,
    ) -> entities.review.ReviewId:
        return await self._review_repository.create_review(
            user_id_entity=user_id,
            movie_id_entity=movie_id,
            contents_entity=review_contents,
        )
