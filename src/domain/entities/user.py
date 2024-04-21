from common import StrictBaseModel


class Credentials(StrictBaseModel):
    username: str
    password: str
