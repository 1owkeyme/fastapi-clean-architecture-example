from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors
from . import errors as err


class GetUserByIdUsecase:
    def __init__(self, user_repository: interfaces.repositories.UserRepository) -> None:
        self._user_repository = user_repository

    @handle_usecases_errors
    async def execute(self, user_id: entities.Id) -> entities.user.UserPublic:
        try:
            return await self._user_repository.get_user_by_id(id_entity=user_id)
        except interfaces.repositories.user_errors.UserNotFoundError:
            raise err.UserNotFoundError from None
