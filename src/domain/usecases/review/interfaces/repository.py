from abc import ABC, abstractmethod

from domain import entities


class ReviewRepository(ABC):
    @abstractmethod
    async def create_review(
        self,
        info_entity: entities.review.ReviewInfo,
    ) -> None:
        pass

    @abstractmethod
    async def delete_review(
        self,
        id_entity: entities.review.ReviewId,
    ) -> None:
        pass
