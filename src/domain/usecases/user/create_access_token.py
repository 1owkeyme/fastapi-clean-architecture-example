from datetime import timedelta

from domain import entities
from domain.interfaces import security as security_interfaces

from . import interfaces


class CreateUserAccessTokenUsecase:
    def __init__(
        self,
        user_repository: interfaces.UserRepository,
        token_service: security_interfaces.TokenService,
        secret: str,
        access_token_expires_delta: timedelta,
    ) -> None:
        self._user_repository = user_repository
        self._token_service = token_service
        self._secret = secret
        self._access_token_expires_delta = access_token_expires_delta

    async def execute(self, user_id: entities.user.UserId) -> entities.auth.AccessToken:
        return self._token_service.create_access_token(
            user_id=user_id,
            expires_delta=self._access_token_expires_delta,
            secret=self._secret,
        )
