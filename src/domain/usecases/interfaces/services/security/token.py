from abc import ABC, abstractmethod
from datetime import timedelta

from domain import entities


ALGORITHM = "HS256"


class TokenService(ABC):
    @staticmethod
    @abstractmethod
    def create_access_token(
        user_id: entities.Id,
        expires_delta: timedelta,
        secret: str,
    ) -> entities.auth.AccessToken:
        pass

    @staticmethod
    @abstractmethod
    def read_access_token(token: entities.auth.AccessToken, secret: str) -> entities.Id:
        pass
