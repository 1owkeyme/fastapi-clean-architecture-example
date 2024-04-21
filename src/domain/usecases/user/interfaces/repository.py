from abc import ABC, abstractmethod

from domain import entities


class UserRepository(ABC):
    @abstractmethod
    async def create_user(
        self,
        safe_credentials: entities.user.SafeCredentials,
    ) -> None:
        pass
