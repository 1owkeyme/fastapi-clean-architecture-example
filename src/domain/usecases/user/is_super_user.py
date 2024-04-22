from domain import entities

from . import interfaces
from .interfaces import errors as err
from .interfaces import repository_errors


class IsUserSuperUserUsecase:
    def __init__(self, user_repository: interfaces.UserRepository) -> None:
        self._user_repository = user_repository

    async def execute(self, user_id: entities.user.UserId) -> bool:
        try:
            user_private = await self._user_repository.get_user_private_by_id(user_id)
        except repository_errors.UserNotFoundError:
            raise err.InvalidCredentialsError from None

        return user_private.is_super_user
