import typing as t
from datetime import timedelta

from pydantic import Field

from common import StrictBaseModel
from domain import entities

from .id_ import Id


class MovieInfo(StrictBaseModel):
    title: str = Field(examples=["Shrek"])
    duration: timedelta = Field(strict=False, examples=["P0DT1H29M0S"])

    def to_movie_info_entity(self) -> entities.movie.MovieInfo:
        return entities.movie.MovieInfo(
            title=self.title,
            duration=self.duration,
        )


class Movie(Id, MovieInfo):
    @classmethod
    def from_movie_entity(cls, movie: entities.movie.Movie) -> t.Self:
        return cls(
            id=movie.id,
            title=movie.title,
            duration=movie.duration,
        )


class CreateMovie(MovieInfo):
    pass


class MovieId(StrictBaseModel):
    movie_id: int = Field(gt=0, examples=[122])

    @classmethod
    def from_id_entity(cls, entity: entities.Id) -> t.Self:
        return cls(movie_id=entity.id)
