from abc import ABC, abstractmethod

from domain import entities


class ReviewRepository(ABC):
    @abstractmethod
    async def create_review(self, info: entities.review.ReviewInfo) -> None:
        pass

    @abstractmethod
    async def delete_review(self, id_: entities.review.ReviewId) -> None:
        pass
