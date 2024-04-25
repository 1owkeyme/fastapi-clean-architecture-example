from domain import entities

from .. import interfaces
from ..error_handlers import handle_usecases_errors
from . import errors as err


class ReadUserAccessTokenUsecase:
    def __init__(
        self,
        user_repository: interfaces.repositories.UserRepository,
        token_service: interfaces.services.security.TokenService,
        secret: str,
    ) -> None:
        self._user_repository = user_repository
        self._token_service = token_service
        self._secret = secret

    @handle_usecases_errors
    async def execute(self, token: entities.auth.AccessToken) -> entities.Id:
        try:
            return self._token_service.read_access_token(token=token, secret=self._secret)
        except interfaces.services.security.token_errors.TokenServiceError:
            raise err.InvalidCredentialsError from None
