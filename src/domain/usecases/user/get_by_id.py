from domain import entities

from .. import interfaces


class GetUserByIdUsecase:
    def __init__(self, user_repository: interfaces.repositories.UserRepository) -> None:
        self._user_repository = user_repository

    async def execute(self, user_id: entities.Id) -> entities.user.UserPublic | None:
        try:
            return await self._user_repository.get_user_by_id(id_entity=user_id)
        except interfaces.repositories.user_errors.UserNotFoundError:
            return None
