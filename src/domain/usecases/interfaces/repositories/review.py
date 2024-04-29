from abc import ABC, abstractmethod

from domain import entities


class ReviewRepository(ABC):
    @abstractmethod
    async def get_review_by_id(self, id_entity: entities.Id) -> entities.review.Review:
        pass

    @abstractmethod
    async def create_review_by_movie_id(
        self,
        user_id_entity: entities.Id,
        movie_id_entity: entities.Id,
        info_entity: entities.review.ReviewInfo,
    ) -> entities.Id:
        pass

    @abstractmethod
    async def delete_review_by_id(self, id_entity: entities.Id) -> entities.Id:
        pass
