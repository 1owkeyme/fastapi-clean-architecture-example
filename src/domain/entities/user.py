import typing as t

from common import StrictBaseModel
from domain.interfaces import security as security_interfaces


class UserId(StrictBaseModel):
    id: int


class Username(StrictBaseModel):
    username: str


class PlainCredentials(Username):
    password: str


class SafeCredentials(Username):
    hashed_password_hex: str

    @classmethod
    def from_plain_credentials(
        cls,
        plain_credentials: PlainCredentials,
        hash_service: security_interfaces.PasswordService,
    ) -> t.Self:
        return cls(
            username=plain_credentials.username,
            hashed_password_hex=hash_service.hash_utf8_password_to_hex(
                plain_credentials.password,
            ),
        )


class UserPublic(UserId, Username):
    pass


class UserPrivate(UserId, SafeCredentials):
    pass
