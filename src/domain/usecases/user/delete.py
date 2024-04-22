from domain import entities

from . import interfaces


class DeleteUserUsecase:
    def __init__(self, user_repository: interfaces.UserRepository) -> None:
        self._user_repository = user_repository

    async def execute(self, user_id: entities.user.UserId) -> None:
        await self._user_repository.delete_user(id_entity=user_id)
