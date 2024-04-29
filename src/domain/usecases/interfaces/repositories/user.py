from abc import ABC, abstractmethod

from domain import entities


class UserRepository(ABC):
    @abstractmethod
    async def get_user_by_id(self, id_entity: entities.Id) -> entities.user.UserPublic:
        pass

    @abstractmethod
    async def get_user_private_by_id(self, id_entity: entities.Id) -> entities.user.UserPrivate:
        pass

    @abstractmethod
    async def get_user_private_by_username(self, username_entity: entities.user.Username) -> entities.user.UserPrivate:
        pass

    @abstractmethod
    async def get_all_users(self) -> list[entities.user.UserPublic]:
        pass

    @abstractmethod
    async def create_user(
        self,
        safe_credentials_entity: entities.user.SafeCredentials,
        is_super_user: bool,
    ) -> entities.Id:
        pass

    @abstractmethod
    async def delete_user_by_id(self, id_entity: entities.Id) -> entities.Id:
        pass

    @abstractmethod
    async def get_all_user_reviews_by_id(self, id_entity: entities.Id) -> list[entities.review.ReviewForUser]:
        pass
