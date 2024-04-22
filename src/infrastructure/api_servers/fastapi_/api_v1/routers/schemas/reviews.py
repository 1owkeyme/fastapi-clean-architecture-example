from pydantic import Field

from common import StrictBaseModel
from domain import entities


class CreateReviewSchema(StrictBaseModel):
    username: str = Field(examples=["Frank"])
    password: str = Field(examples=["C0wperw00d"])

    def to_user_plain_credentials_entity(
        self,
    ) -> entities.user.PlainCredentials:
        return entities.user.PlainCredentials(
            username=self.username,
            password=self.password,
        )
