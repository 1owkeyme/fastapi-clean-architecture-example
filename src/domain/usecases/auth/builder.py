from .. import interfaces
from .sign_in import SignInUsecase
from .sign_up import SignUpUsecase


class AuthUsecasesBuilder:
    def __init__(
        self,
        user_repository: interfaces.repositories.UserRepository,
    ) -> None:
        self.__user_repository = user_repository

    def create_sign_up_usecase(self) -> SignUpUsecase:
        return SignUpUsecase(user_repository=self.__user_repository)

    def create_sign_in_usecase(self) -> SignInUsecase:
        return SignInUsecase()
