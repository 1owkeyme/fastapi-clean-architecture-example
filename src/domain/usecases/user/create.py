from domain import entities
from domain.usecases.interfaces import security as security_interfaces

from . import interfaces


class CreateUserUsecase:
    def __init__(
        self,
        user_repository: interfaces.UserRepository,
        hash_service: security_interfaces.PasswordService,
    ) -> None:
        self._user_repository = user_repository
        self._hash_service = hash_service

    async def execute(self, user_plain_credentials: entities.user.PlainCredentials) -> entities.user.UserId:
        safe_credentials = entities.user.SafeCredentials(
            username=user_plain_credentials.username,
            hashed_password_hex=self._hash_service.hash_utf8_password_to_hex(user_plain_credentials.password),
        )

        return await self._user_repository.create_user(safe_credentials_entity=safe_credentials)
