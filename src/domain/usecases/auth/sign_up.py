from domain import entities

from . import interfaces


class SignUpUsecase:
    def __init__(self, user_repository: interfaces.UserRepository) -> None:
        self._user_repository = user_repository

    async def execute(
        self,
        user_credentials: entities.user.Credentials,
    ) -> None:
        await self._user_repository.create_user(credentials=user_credentials)
