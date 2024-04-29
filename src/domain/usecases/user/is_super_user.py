from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors
from . import errors as err


class IsUserSuperUserUsecase:
    def __init__(self, user_repository: interfaces.repositories.UserRepository) -> None:
        self._user_repository = user_repository

    @handle_usecases_errors
    async def execute(self, user_id: entities.Id) -> bool:
        try:
            user_private = await self._user_repository.get_user_private_by_id(user_id)
        except interfaces.repositories.user_errors.UserNotFoundError:
            raise err.UserNotFoundError from None

        return user_private.is_super_user
