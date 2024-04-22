from abc import ABC, abstractmethod

from domain import entities


class UserRepository(ABC):
    @abstractmethod
    async def get_user_by_id(self, id_entity: entities.user.UserId) -> entities.user.UserPublic:
        pass

    @abstractmethod
    async def get_all_users(self) -> list[entities.user.UserPublic]:
        pass

    @abstractmethod
    async def create_user(self, safe_credentials_entity: entities.user.SafeCredentials) -> entities.user.UserId:
        pass

    @abstractmethod
    async def delete_user(self, id_entity: entities.user.UserId) -> None:
        pass

    @abstractmethod
    async def get_all_user_reviews(self, id_entity: entities.user.UserId) -> list[entities.review.ReviewForUser]:
        pass
