from domain import entities

from .. import interfaces


class IsUserSuperUserUsecase:
    def __init__(self, user_repository: interfaces.repositories.UserRepository) -> None:
        self._user_repository = user_repository

    async def execute(self, user_id: entities.Id) -> bool:
        user_private = await self._user_repository.get_user_private_by_id(user_id)

        return user_private.is_super_user
