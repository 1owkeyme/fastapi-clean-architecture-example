from __future__ import annotations

import typing as t

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship
from sqlalchemy.types import String

from domain import entities

from .base import Base
from .constants import TableName


if t.TYPE_CHECKING:
    from .review import Review


class User(Base):
    __tablename__ = TableName.USERS

    username: Mapped[str] = mapped_column(String(32), unique=True)
    hashed_password_hex: Mapped[str] = mapped_column(String(120))

    reviews: Mapped[list[Review]] = relationship(back_populates="user")

    def to_user_public_entity(self) -> entities.user.UserPublic:
        return entities.user.UserPublic(id=self.id, username=self.username)


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
