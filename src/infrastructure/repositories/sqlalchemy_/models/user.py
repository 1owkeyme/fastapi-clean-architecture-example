import typing as t

from sqlalchemy import ForeignKey, false
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship
from sqlalchemy.types import Boolean, String

from common import StrictBaseModel
from domain import entities

from .base import Base
from .constants import TableName


if t.TYPE_CHECKING:
    from .review import Review


class User(Base):
    __tablename__ = TableName.USERS

    username: Mapped[str] = mapped_column(String(32), unique=True)
    hashed_password_hex: Mapped[str] = mapped_column(String(120))
    is_super_user: Mapped[bool] = mapped_column(Boolean, default=False, server_default=false())

    reviews: Mapped[list["Review"]] = relationship(back_populates="user")

    def to_user_public_entity(self) -> entities.user.UserPublic:
        return entities.user.UserPublic(id=self.id, username=self.username)

    def to_user_private_entity(self) -> entities.user.UserPrivate:
        return entities.user.UserPrivate(
            id=self.id,
            username=self.username,
            hashed_password_hex=self.hashed_password_hex,
            is_super_user=self.is_super_user,
        )

    def to_user_id_entity(self) -> entities.user.UserId:
        return entities.user.UserId(id=self.id)


class UserRelationMixin:
    _user_id_unique: bool = False
    _user_id_nullable: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    @classmethod
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(User.id),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
            name="user_id",
        )

    @declared_attr
    @classmethod
    def user(cls) -> Mapped[User]:
        return relationship(back_populates=cls._user_back_populates)


class UserId(StrictBaseModel):
    id: int

    @classmethod
    def from_entity(cls, entity: entities.user.UserId) -> t.Self:
        return cls(id=entity.id)


class Username(StrictBaseModel):
    username: str

    @classmethod
    def from_entity(cls, entity: entities.user.Username) -> t.Self:
        return cls(username=entity.username)
