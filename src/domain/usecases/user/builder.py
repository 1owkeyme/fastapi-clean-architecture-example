from .. import interfaces
from .create import CreateUserUsecase
from .delete_by_id import DeleteUserByIdUsecase
from .get_all import GetAllUsersUsecase
from .get_all_reviews_by_id import GetAllUserReviewsByIdUsecase
from .get_by_id import GetUserByIdUsecase
from .is_super_user import IsUserSuperUserUsecase


class UserUsecasesBuilder:
    def __init__(
        self,
        user_repository: interfaces.repositories.UserRepository,
        password_service: interfaces.services.security.PasswordService,
        first_super_user_username: str,
    ) -> None:
        self._user_repository = user_repository

        self._password_service = password_service

        self._first_super_user_username = first_super_user_username

    def construct_create_user_usecase(self) -> CreateUserUsecase:
        return CreateUserUsecase(
            user_repository=self._user_repository,
            password_service=self._password_service,
        )

    def construct_delete_user_by_id_usecase(self) -> DeleteUserByIdUsecase:
        return DeleteUserByIdUsecase(
            user_repository=self._user_repository,
            first_super_user_username=self._first_super_user_username,
        )

    def construct_get_all_users_usecase(self) -> GetAllUsersUsecase:
        return GetAllUsersUsecase(user_repository=self._user_repository)

    def construct_get_all_user_reviews_by_id_usecase(self) -> GetAllUserReviewsByIdUsecase:
        return GetAllUserReviewsByIdUsecase(user_repository=self._user_repository)

    def construct_get_user_by_id_usecase(self) -> GetUserByIdUsecase:
        return GetUserByIdUsecase(user_repository=self._user_repository)

    def construct_is_user_super_user_usecase(self) -> IsUserSuperUserUsecase:
        return IsUserSuperUserUsecase(user_repository=self._user_repository)
