from domain.interfaces import security as security_interfaces

from . import interfaces
from .create import CreateUserUsecase
from .delete import DeleteUserUsecase
from .get_all import GetAllUsersUsecase
from .get_all_reviews import GetAllUserReviewsUsecase
from .get_by_id import GetUserByIdUsecase


class UserUsecasesBuilder:
    def __init__(
        self,
        user_repository: interfaces.UserRepository,
        hash_service: security_interfaces.HashService,
    ) -> None:
        self._user_repository = user_repository
        self._hash_service = hash_service

    def construct_create_user_usecase(self) -> CreateUserUsecase:
        return CreateUserUsecase(
            user_repository=self._user_repository,
            hash_service=self._hash_service,
        )

    def construct_delete_user_usecase(self) -> DeleteUserUsecase:
        return DeleteUserUsecase(user_repository=self._user_repository)

    def construct_get_all_users_usecase(self) -> GetAllUsersUsecase:
        return GetAllUsersUsecase(user_repository=self._user_repository)

    def construct_get_all_user_reviews_usecase(self) -> GetAllUserReviewsUsecase:
        return GetAllUserReviewsUsecase(user_repository=self._user_repository)

    def construct_get_user_by_id_usecase(self) -> GetUserByIdUsecase:
        return GetUserByIdUsecase(user_repository=self._user_repository)
