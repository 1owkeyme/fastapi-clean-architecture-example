from domain import entities

from .. import interfaces


class DeleteUserByIdUsecase:
    def __init__(self, user_repository: interfaces.repositories.UserRepository) -> None:
        self._user_repository = user_repository

    async def execute(self, user_id: entities.Id) -> entities.Id:
        return await self._user_repository.delete_user_by_id(id_entity=user_id)
