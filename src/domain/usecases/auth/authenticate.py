from domain import entities

from .. import interfaces
from . import errors as err


class AuthenticateUserUsecase:
    def __init__(
        self,
        user_repository: interfaces.repositories.UserRepository,
        password_service: interfaces.services.security.PasswordService,
    ) -> None:
        self._user_repository = user_repository
        self._password_service = password_service

    async def execute(self, plain_credentials: entities.user.PlainCredentials) -> entities.Id:
        try:
            user_private = await self._user_repository.get_user_private_by_username(plain_credentials)
        except interfaces.repositories.user_errors.UserNotFoundError:
            raise err.InvalidCredentialsError from None

        is_password_valid = self._password_service.check_utf8_password(
            plain_credentials.password,
            hashed_password_hex=user_private.hashed_password_hex,
        )

        if not is_password_valid:
            raise err.InvalidCredentialsError

        return user_private
