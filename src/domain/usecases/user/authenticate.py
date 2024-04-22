from domain import entities
from domain.interfaces import security as security_interfaces

from . import interfaces
from .interfaces import errors as err
from .interfaces import repository_errors


class AuthenticateUserUsecase:
    def __init__(
        self,
        user_repository: interfaces.UserRepository,
        hash_service: security_interfaces.HashService,
    ) -> None:
        self._user_repository = user_repository
        self._hash_serivce = hash_service

    async def execute(self, plain_credentials: entities.user.PlainCredentials) -> entities.user.UserId:
        try:
            user_private = await self._user_repository.get_user_private_by_username(plain_credentials)
        except repository_errors.UserNotFoundError:
            raise err.InvalidCredentialsError from None

        is_password_valid = self._hash_serivce.check_utf8_password(
            plain_credentials.password,
            hashed_password_hex=user_private.hashed_password_hex,
        )

        if not is_password_valid:
            raise err.InvalidCredentialsError

        return user_private
