from abc import ABC, abstractmethod

from domain import entities


class UserRepository(ABC):
    @abstractmethod
    async def get_all_users(self) -> list[entities.user.UserPublic]:
        pass

    @abstractmethod
    async def create_user(
        self,
        safe_credentials_entity: entities.user.SafeCredentials,
    ) -> None:
        pass

    @abstractmethod
    async def delete_user(
        self,
        id_entity: entities.user.UserId,
    ) -> None:
        pass
