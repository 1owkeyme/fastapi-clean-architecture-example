import typing as t
from datetime import timedelta

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship
from sqlalchemy.types import Interval, String

from domain import entities

from .base import Base
from .constants import TableName
from .id_ import Id


if t.TYPE_CHECKING:
    from .review import Review


class MovieInfo(Base):
    __abstract__ = True

    title: Mapped[str] = mapped_column(String(50), unique=True)
    duration: Mapped[timedelta] = mapped_column(Interval())

    @classmethod
    def movie_info_from_entity(cls, entity: entities.movie.MovieInfo) -> t.Self:
        return cls(title=entity.title, duration=entity.duration)


class Movie(Id, MovieInfo):
    __tablename__ = TableName.MOVIES

    reviews: Mapped[list["Review"]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan",
    )

    def to_movie_entity(self) -> entities.movie.Movie:
        return entities.movie.Movie(id=self.id, title=self.title, duration=self.duration)


class MovieRelationMixin:
    _movie_id_unique: bool = False
    _movie_id_nullable: bool = False
    _movie_back_populates: str | None = None
    _many_to_one_movie: bool = False

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
        return relationship(back_populates=cls._movie_back_populates, innerjoin=cls._many_to_one_movie)
