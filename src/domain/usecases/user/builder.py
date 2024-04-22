from datetime import timedelta

from domain.usecases.interfaces import security as security_interfaces

from . import interfaces
from .authenticate import AuthenticateUserUsecase
from .create import CreateUserUsecase
from .create_access_token import CreateUserAccessTokenUsecase
from .delete import DeleteUserUsecase
from .get_all import GetAllUsersUsecase
from .get_all_reviews import GetAllUserReviewsUsecase
from .get_by_id import GetUserByIdUsecase
from .is_super_user import IsUserSuperUserUsecase
from .read_access_token import ReadUserAccessTokenUsecase


class UserUsecasesBuilder:
    def __init__(
        self,
        user_repository: interfaces.UserRepository,
        hash_service: security_interfaces.PasswordService,
        token_service: security_interfaces.TokenService,
        secret: str,
        access_token_expires_minutes: int,
    ) -> None:
        self._user_repository = user_repository

        self._hash_service = hash_service

        self._token_serivice = token_service
        self._secret = secret
        self._access_token_expires_delta = timedelta(minutes=access_token_expires_minutes)

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

    def construct_authenticate_user_usecase(self) -> AuthenticateUserUsecase:
        return AuthenticateUserUsecase(user_repository=self._user_repository, hash_service=self._hash_service)

    def construct_create_user_access_token_usecase(self) -> CreateUserAccessTokenUsecase:
        return CreateUserAccessTokenUsecase(
            user_repository=self._user_repository,
            token_service=self._token_serivice,
            secret=self._secret,
            access_token_expires_delta=self._access_token_expires_delta,
        )

    def construct_read_user_access_token_usecase(self) -> ReadUserAccessTokenUsecase:
        return ReadUserAccessTokenUsecase(
            user_repository=self._user_repository,
            token_service=self._token_serivice,
            secret=self._secret,
        )

    def construct_is_user_super_user_usecase(self) -> IsUserSuperUserUsecase:
        return IsUserSuperUserUsecase(user_repository=self._user_repository)
