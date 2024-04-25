from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors
from . import errors as err


class DeleteUserByIdUsecase:
    def __init__(
        self,
        user_repository: interfaces.repositories.UserRepository,
        first_super_user_username: str,
    ) -> None:
        self._user_repository = user_repository

        self._first_super_user_username = first_super_user_username

    @handle_usecases_errors
    async def execute(self, user_id: entities.Id) -> entities.Id:
        try:
            user = await self._user_repository.get_user_by_id(user_id)
        except interfaces.repositories.user_errors.UserNotFoundError:
            raise err.UserNotFoundError from None

        if user.username == self._first_super_user_username:
            raise err.FirstSuperUserDeleteForbiddenError

        try:
            return await self._user_repository.delete_user_by_id(id_entity=user_id)
        except interfaces.repositories.user_errors.UserNotFoundError:  # race is possible so checking second time
            raise err.UserNotFoundError from None
