from common import StrictBaseModel

from .id_ import Id


class Username(StrictBaseModel):
    username: str


class PlainCredentials(Username):
    password: str


class SafeCredentials(Username):
    hashed_password_hex: str


class UserPublic(Id, Username):
    pass


class UserPrivate(Id, SafeCredentials):
    is_super_user: bool
