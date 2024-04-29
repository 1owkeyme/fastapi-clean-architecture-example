from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors


class GetAllUsersUsecase:
    def __init__(self, user_repository: interfaces.repositories.UserRepository) -> None:
        self._user_repository = user_repository

    @handle_usecases_errors
    async def execute(self) -> list[entities.user.UserPublic]:
        return await self._user_repository.get_all_users()
