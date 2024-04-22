from domain import entities

from . import interfaces


class GetUserByIdUsecase:
    def __init__(self, user_repository: interfaces.UserRepository) -> None:
        self._user_repository = user_repository

    async def execute(self, user_id: entities.user.UserId) -> entities.user.UserPublic:
        return await self._user_repository.get_user_by_id(id_entity=user_id)
