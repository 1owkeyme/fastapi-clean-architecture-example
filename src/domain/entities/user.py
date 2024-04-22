from common import StrictBaseModel


class UserId(StrictBaseModel):
    id: int


class Username(StrictBaseModel):
    username: str


class PlainCredentials(Username):
    password: str


class SafeCredentials(Username):
    hashed_password_hex: str


class UserPublic(UserId, Username):
    pass


class UserPrivate(UserId, SafeCredentials):
    is_super_user: bool
