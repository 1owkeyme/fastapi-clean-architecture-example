from domain.interfaces import security as security_interfaces

from . import interfaces
from .create import CreateUserUsecase
from .sign_in import SignInUsecase


class UserUsecasesBuilder:
    def __init__(
        self,
        user_repository: interfaces.UserRepository,
        hash_service: security_interfaces.HashService,
    ) -> None:
        self._user_repository = user_repository
        self._hash_service = hash_service

    def construct_sign_up_usecase(self) -> CreateUserUsecase:
        return CreateUserUsecase(
            user_repository=self._user_repository,
            hash_service=self._hash_service,
        )

    def construct_sign_in_usecase(self) -> SignInUsecase:
        return SignInUsecase()
