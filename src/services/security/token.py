from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt  # type:ignore[import-untyped]
from pydantic import ValidationError

from common import StrictBaseModel
from domain import entities
from domain.usecases.interfaces import security as security_interfaces


class TokenPayload(StrictBaseModel):
    exp: timedelta
    sub: int


class JWTService(security_interfaces.TokenService):
    @staticmethod
    def create_access_token(
        user_id: entities.user.UserId,
        expires_delta: timedelta,
        secret: str,
    ) -> entities.auth.AccessToken:
        expire = datetime.now(UTC) + expires_delta
        to_encode = {"exp": expire, "sub": user_id.id}
        return jwt.encode(to_encode, secret, algorithm=security_interfaces.token.ALGORITHM)  # type:ignore[no-any-return] # since jose [import-untyped]

    @staticmethod
    def read_access_token(token: entities.auth.AccessToken, secret: str) -> entities.user.UserId:
        try:
            raw_token_payload = jwt.decode(token, secret, algorithms=[security_interfaces.token.ALGORITHM])
            token_payload = TokenPayload(**raw_token_payload)
        except (JWTError, ValidationError) as exc:
            raise security_interfaces.token_errors.InvalidTokenError from exc

        return entities.user.UserId(id=token_payload.sub)
