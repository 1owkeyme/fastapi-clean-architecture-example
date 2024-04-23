from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt  # type:ignore[import-untyped]
from pydantic import ValidationError

from common import StrictBaseModel
from domain import entities
from domain.usecases.interfaces.services import security as security_interfaces


class TokenPayload(StrictBaseModel):
    exp: datetime
    sub: str


class JWTService(security_interfaces.TokenService):
    @staticmethod
    def create_access_token(
        user_id: entities.Id,
        expires_delta: timedelta,
        secret: str,
    ) -> entities.auth.AccessToken:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode = TokenPayload(exp=expire, sub=str(user_id.id)).model_dump()
        return jwt.encode(to_encode, secret, algorithm=security_interfaces.token.ALGORITHM)  # type:ignore[no-any-return] # since jose [import-untyped]

    @staticmethod
    def read_access_token(token: entities.auth.AccessToken, secret: str) -> entities.Id:
        try:
            raw_token_payload = jwt.decode(token, secret, algorithms=[security_interfaces.token.ALGORITHM])
            token_payload = TokenPayload(**raw_token_payload)
        except (JWTError, ValidationError) as exc:
            raise security_interfaces.token_errors.InvalidTokenError from exc

        return entities.Id(id=int(token_payload.sub))
