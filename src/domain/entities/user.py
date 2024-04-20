from common import StrictBaseModel


class User(StrictBaseModel):
    username: str
    hashed_password: str
