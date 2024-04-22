from domain import entities
from domain.interfaces import security as security_interfaces

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
        safe_credentials = entities.user.SafeCredentials.from_plain_credentials(
            plain_credentials=user_plain_credentials,
            hash_service=self._hash_service,
        )

        return await self._user_repository.create_user(safe_credentials_entity=safe_credentials)
