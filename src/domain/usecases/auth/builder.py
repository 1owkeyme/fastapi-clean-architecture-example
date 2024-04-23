from datetime import timedelta

from .. import interfaces
from .authenticate import AuthenticateUserUsecase
from .create_access_token import CreateUserAccessTokenUsecase
from .read_access_token import ReadUserAccessTokenUsecase


class AuthUsecasesBuilder:
    def __init__(
        self,
        user_repository: interfaces.repositories.UserRepository,
        password_service: interfaces.services.security.PasswordService,
        token_service: interfaces.services.security.TokenService,
        secret: str,
        access_token_expires_minutes: int,
    ) -> None:
        self._user_repository = user_repository

        self._password_service = password_service

        self._token_serivice = token_service
        self._secret = secret
        self._access_token_expires_delta = timedelta(minutes=access_token_expires_minutes)

    def construct_authenticate_user_usecase(self) -> AuthenticateUserUsecase:
        return AuthenticateUserUsecase(user_repository=self._user_repository, password_service=self._password_service)

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
