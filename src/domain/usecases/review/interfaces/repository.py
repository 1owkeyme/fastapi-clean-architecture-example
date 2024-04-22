from abc import ABC, abstractmethod

from domain import entities


class ReviewRepository(ABC):
    @abstractmethod
    async def get_review_by_id(self, id_entity: entities.review.ReviewId) -> entities.review.Review:
        pass

    @abstractmethod
    async def create_review(
        self,
        user_id_entity: entities.user.UserId,
        movie_id_entity: entities.movie.MovieId,
        contents_entity: entities.review.ReviewContents,
    ) -> entities.review.ReviewId:
        pass

    @abstractmethod
    async def delete_review(self, id_entity: entities.review.ReviewId) -> entities.review.ReviewId:
        pass
