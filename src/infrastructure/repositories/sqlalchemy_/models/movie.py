from __future__ import annotations

import typing as t
from datetime import timedelta

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship
from sqlalchemy.types import Interval, String

from .base import Base
from .constants import TableName


if t.TYPE_CHECKING:
    from .review import Review


class Movie(Base):
    __tablename__ = TableName.MOVIES

    title: Mapped[str] = mapped_column(String(50), unique=True)
    duration: Mapped[timedelta] = mapped_column(Interval())

    reviews: Mapped[list[Review]] = relationship(back_populates="movie")


class MovieRelationMixin:
    _movie_id_unique: bool = False
    _movie_id_nullable: bool = False
    _movie_back_populates: str | None = None

    @declared_attr
    @classmethod
    def movie_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(Movie.id),
            unique=cls._movie_id_unique,
            nullable=cls._movie_id_nullable,
            name="movie_id",
        )

    @declared_attr
    @classmethod
    def movie(cls) -> Mapped[Movie]:
        return relationship(back_populates=cls._movie_back_populates)
