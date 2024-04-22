import typing as t
from datetime import timedelta

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship
from sqlalchemy.types import Interval, String

from common import StrictBaseModel
from domain import entities

from .base import Base
from .constants import TableName


if t.TYPE_CHECKING:
    from .review import Review


class Movie(Base):
    __tablename__ = TableName.MOVIES

    title: Mapped[str] = mapped_column(String(50), unique=True)
    duration: Mapped[timedelta] = mapped_column(Interval())

    reviews: Mapped[list["Review"]] = relationship(back_populates="movie")

    @classmethod
    def from_movie_info_entity(cls, movie_info: entities.movie.MovieInfo) -> t.Self:
        return cls(title=movie_info.title, duration=movie_info.duration)

    def to_movie_entity(self) -> entities.movie.Movie:
        return entities.movie.Movie(id=self.id, title=self.title, duration=self.duration)

    def to_movie_id_entity(self) -> entities.movie.MovieId:
        return entities.movie.MovieId(id=self.id)


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


class MovieId(StrictBaseModel):
    id: int

    @classmethod
    def from_movie_id_entity(cls, movie_id_entity: entities.movie.MovieId) -> t.Self:
        return cls(id=movie_id_entity.id)
