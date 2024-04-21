from pydantic import Field

from common import StrictBaseModel
from domain import entities


class SignUpUserSchema(StrictBaseModel):
    username: str = Field(examples=["Frank"])
    password: str = Field(examples=["C0wperw00d"])

    def to_user_credentials_entity(self) -> entities.user.Credentials:
        return entities.user.Credentials(
            username=self.username,
            password=self.password,
        )
