from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors
from . import errors as err


class CreateUserUsecase:
    def __init__(
        self,
        user_repository: interfaces.repositories.UserRepository,
        password_service: interfaces.services.security.PasswordService,
    ) -> None:
        self._user_repository = user_repository
        self._password_service = password_service

    @handle_usecases_errors
    async def execute(
        self,
        user_plain_credentials: entities.user.PlainCredentials,
        is_super_user: bool = False,
    ) -> entities.Id:
        safe_credentials = entities.user.SafeCredentials(
            username=user_plain_credentials.username,
            hashed_password_hex=self._password_service.hash_utf8_password_to_hex(user_plain_credentials.password),
        )
        try:
            return await self._user_repository.create_user(
                safe_credentials_entity=safe_credentials,
                is_super_user=is_super_user,
            )
        except interfaces.repositories.user_errors.UserAlreadyExistsError:
            raise err.UserAlreadyExistsError from None
